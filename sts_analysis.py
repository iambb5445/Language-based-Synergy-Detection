from llm_connector import LLMConnector, OpenAILib, OpenAIChat, GeminiChat
from joblib import delayed, Parallel
from tqdm import tqdm
from sts_prompts import get_sts_prompts, get_single_card_ask, get_multi_card_multi_ask, get_multi_card_bundle_ask, get_multi_card_bundle_no_local_ask, AskType
from utility import TextUtil
from subset import subrows

thread_count = 61
SHOULD_SUBSET = False
RETRY_COUNT = 3

class IncorrectResponseLengthException(Exception):
    def __init__(self, length, expected_length, response):
        super().__init__(f"Incorrecnt length of {length}, expected {expected_length}, for {response[:100] + ' ... ' + response[-100:]}")

def ask_until_format_is_right(chat, prompt, bundle_size:None|int=None):
    # mock answer (NaN)
    # return ('NaN\n---NEXT---\n' * (bundle_size-1) + 'NaN\n') if bundle_size is not None else 'NaN\n'
    # mock answer (4)
    # return ('4\n---NEXT---\n' * (bundle_size-1) + '4\n') if bundle_size is not None else '4\n'
    result = chat.ask(prompt)
    for i in range(RETRY_COUNT):
        try:
            if bundle_size is not None:
                vals = [float((r.split()[-1]) if len(r) > 0 else r) for r in result.split('---NEXT---')]
                if len(vals) != bundle_size:
                    raise IncorrectResponseLengthException(len(vals), bundle_size, result)
            else:
                float(result.split()[-1])
            break
        except (ValueError, IncorrectResponseLengthException, IndexError) as e:
            if len(result) == 0:
                print("Empty result: connection error")
                i -= 1
            else:
                print(f"Unacceptable response for \"{prompt}\"")
                print(result)
                print(f"Exception: {e}")
            if i == RETRY_COUNT - 1:
                result = f'invalid response {RETRY_COUNT} times\n[latest] {result.replace("---NEXT---", "<NEXT_TOKEN_REPLACED>")}\nNaN\n' * (1 if bundle_size is None else bundle_size)
                result += f'---NEXT---\nNaN\n' * (0 if bundle_size is None else (bundle_size - 1))
            else:
                result = chat.ask(prompt)
    return result

def get_request_and_response(chat, card1, card2, id1, id2, starting_card_number):
        prompt, id, _ = get_single_card_ask(card1, card2, id1, id2, starting_card_number)
        result = ask_until_format_is_right(chat, prompt)
        return prompt, result, id
    
# TODO change the type to LLMConnector instead of OpenAIChat
def get_multi_request_and_response(chat: OpenAILib, x_cards, y_cards, x_indices, y_indices, starting_card_number):
    prompts, ids, _ = get_multi_card_multi_ask(x_cards, y_cards, x_indices, y_indices, starting_card_number)
    results = []
    chat = chat.copy()
    chat.chat_format = True
    for prompt in prompts:
        result = ask_until_format_is_right(chat, prompt)
        results.append(result)
    return prompts, results, ids

def get_bundle_request_and_response(chat: LLMConnector, x_cards, y_cards, x_indices, y_indices, starting_card_number):
    prompt, ids, _ = get_multi_card_bundle_ask(x_cards, y_cards, x_indices, y_indices, starting_card_number)
    # print(TextUtil.get_colored_text(f"{x_indices} x {y_indices}\n", TextUtil.TEXT_COLOR.Red))
    # print(TextUtil.get_colored_text(prompt, TextUtil.TEXT_COLOR.Yellow))
    results = ask_until_format_is_right(chat, prompt, len(x_cards) * len(y_cards)).split('---NEXT---')
    # print(TextUtil.get_colored_text('\n&\n'.join(results), TextUtil.TEXT_COLOR.Blue))
    return prompt, results, ids

def get_bundle_no_local_request_and_response(chat: LLMConnector, card_pairs, index_pairs, starting_card_number):
    prompt, ids, _ = get_multi_card_bundle_no_local_ask(card_pairs, index_pairs, starting_card_number)
    # print(TextUtil.get_colored_text(f"{x_indices} x {y_indices}\n", TextUtil.TEXT_COLOR.Red))
    # print(TextUtil.get_colored_text(prompt, TextUtil.TEXT_COLOR.Yellow))
    results = ask_until_format_is_right(chat, prompt, len(card_pairs)).split('---NEXT---')
    # print(TextUtil.get_colored_text('\n&\n'.join(results), TextUtil.TEXT_COLOR.Blue))
    return prompt, results, ids

def log(prompt, response, output_filename, tag=""):
    with open(f"{output_filename}.log", "a", encoding='utf-8') as f:
        f.write(prompt+'\n')
        f.write(tag + response)
        f.write('\n-------------------------------------------------------------\n')

def run_single_ask_job(chat, cards_df, next_card_number):
    queries = [(row1, row2, index1, index2) for index1, row1 in cards_df.iterrows() for index2, row2 in cards_df.iterrows()]
    if SHOULD_SUBSET:
        queries = [query for query in queries if query[2] in subrows and query[3] in subrows]
    req_responses = Parallel(n_jobs=thread_count)(delayed(get_request_and_response)(chat, queries[i][0], queries[i][1], queries[i][2], queries[i][3], next_card_number) for i in tqdm(range(len(queries))))
    assert isinstance(req_responses, list), "Parallel jobs have not resulted in an output of type list"
    assert None not in req_responses
    return req_responses

def run_multi_ask_job(chat, cards_df, card_count, next_card_number):
    parts = []
    for index, row in cards_df.iterrows():
        if SHOULD_SUBSET and index not in subrows:
            continue
        if len(parts) == 0 or len(parts[-1][0]) >= card_count:
            parts.append(([], []))
        parts[-1][0].append(index)
        parts[-1][1].append(row)
    queries = [(x_cards, y_cards, x, y) for x, x_cards in parts for y, y_cards in parts]
    req_responses = Parallel(n_jobs=thread_count)(delayed(get_multi_request_and_response)(chat, queries[i][0], queries[i][1], queries[i][2], queries[i][3], next_card_number) for i in tqdm(range(len(queries))))
    assert isinstance(req_responses, list), "Parallel jobs have not resulted in an output of type list"
    prompts, results, ids = [], [], []
    for chunk_ps, chunk_rs, chunk_is in req_responses: # type: ignore
        prompts += chunk_ps
        results += chunk_rs
        ids += chunk_is
    return zip(prompts, results, ids)

def run_bundle_ask_job(chat, cards_df, card_count, next_card_number):
    parts = []
    for index, row in cards_df.iterrows():
        if SHOULD_SUBSET and index not in subrows:
            continue
        if len(parts) == 0 or len(parts[-1][0]) >= card_count:
            parts.append(([], []))
        parts[-1][0].append(index)
        parts[-1][1].append(row)
    queries = [(x_cards, y_cards, x, y) for x, x_cards in parts for y, y_cards in parts]
    req_responses = Parallel(n_jobs=thread_count)(delayed(get_bundle_request_and_response)(chat, queries[i][0], queries[i][1], queries[i][2], queries[i][3], next_card_number) for i in tqdm(range(len(queries))))
    assert isinstance(req_responses, list), "Parallel jobs have not resulted in an output of type list"
    prompts, results, ids = [], [], []
    for chunk_p, chunk_rs, chunk_is in req_responses: # type: ignore
        prompts += [chunk_p] + ['[continued from last responses]'] * (len(chunk_rs) - 1)
        results += chunk_rs
        ids += chunk_is
    return zip(prompts, results, ids)

def run_bundle_no_local_ask_job(chat, cards_df, eq_bundle_card_count, next_card_number):
    import math
    import random
    eq_bundle_splits = math.ceil(len(cards_df) / eq_bundle_card_count)
    queries = [([], []) for _ in range(eq_bundle_splits) for _ in range(eq_bundle_splits)]
    random.seed(42)
    for index1, row1 in cards_df.iterrows():
        if SHOULD_SUBSET and index1 not in subrows:
            continue
        for index2, row2 in cards_df.iterrows():
            if SHOULD_SUBSET and index2 not in subrows:
                continue
            query = random.choice([query for query in queries if len(query[0]) < eq_bundle_card_count * eq_bundle_card_count])
            query[0].append((row1, row2))
            query[1].append((index1, index2))
    queries = [query for query in queries if len(query[0]) > 0]
    req_responses = Parallel(n_jobs=thread_count)(delayed(get_bundle_no_local_request_and_response)(chat, queries[i][0], queries[i][1], next_card_number) for i in tqdm(range(len(queries))))
    assert isinstance(req_responses, list), "Parallel jobs have not resulted in an output of type list"
    prompts, results, ids = [], [], []
    for chunk_p, chunk_rs, chunk_is in req_responses: # type: ignore
        prompts += [chunk_p] + ['[continued from last responses]'] * (len(chunk_rs) - 1)
        results += chunk_rs
        ids += chunk_is
    return zip(prompts, results, ids)

if __name__=="__main__":
    system_prompt, prompts, responses, next_card_number = get_sts_prompts(ask_type=AskType.Negative_or_Positive_Revised, shot_count=None)
    chat = OpenAIChat(OpenAIChat.OpenAIModel.GPT_4O_mini, chat_format=False, system_message=system_prompt)
    # chat = GeminiChat(GeminiChat.GeminiModel.Gemini_1_Pro, chat_format=False, system_message=system_prompt)
    for prompt, response in zip(prompts, responses):
        chat.inject(prompt, response)
    import pandas as pd
    import numpy as np
    import time
    from utility import get_safe_filename
    output_filename = get_safe_filename(f"synergy_results_{chat.model_identifier}", timed=True)
    df = pd.read_csv("IronClad Card Names.csv")
    # df = df[:6] # Test for first 3 cards only
    df = df.sample(frac=1, random_state=42).reset_index(drop=False) #shuffle
    index_mapping = {new_idx: old_idx for new_idx, old_idx in enumerate(df['index'])}

    synergies = np.empty((len(df), len(df)))
    synergies[:] = np.nan
    for prompt, response in zip(prompts, responses):
        log(prompt, response, output_filename, "[injected]")

    req_responses = run_single_ask_job(chat, df, next_card_number)
    # req_responses = run_multi_ask_job(chat, df, 4, next_card_number)
    # req_responses = run_bundle_ask_job(chat, df, 4, next_card_number) # AskType.NP_Bundle/Revised only!
    # req_responses = run_bundle_no_local_ask_job(chat, df, 4, next_card_number) # AskType.NP_Bundle/Revised only!
    for prompt, result, id in req_responses: # type: ignore
        index1, index2 = id
        log(prompt, result, output_filename)
        try:
            synergies[index_mapping[index1], index_mapping[index2]] = float(result.split()[-1])
        except Exception as e:
            print(f"{e}\nError for {index_mapping[index1]} {index_mapping[index2]}, response: ...{result[-10:]}")
            synergies[index_mapping[index1], index_mapping[index2]] = float("NaN")
    csv_filename = f"{output_filename}{'_subset' if SHOULD_SUBSET else ''}.csv"
    pd.DataFrame(synergies).to_csv(csv_filename)
    print(f"saved as {csv_filename}")
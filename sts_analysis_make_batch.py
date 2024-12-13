from llm_connector import OpenAIChat
from sts_prompts import get_sts_prompts, get_single_card_ask, AskType

break_into = 2

# TODO subset

if __name__=="__main__":
    system_prompt, prompts, responses, next_card_number = get_sts_prompts(ask_type=AskType.Negative_or_Positive)
    chat = OpenAIChat(OpenAIChat.OpenAIModel.GPT_4O_mini, chat_format=False, system_message=system_prompt)
    for prompt, response in zip(prompts, responses):
        chat.inject(prompt, response)
    import pandas as pd
    import numpy as np
    import time
    output_filename = f"batch_job_{chat.model_identifier}_{int(time.time())}"
    df = pd.read_csv("IronClad Card Names.csv")
    # df = df[:3] # Test for first 3 cards only
    json_requests = []
    for index1, card1 in df.iterrows():
        for index2, card2 in df.iterrows():    
            prompt, _, _ = get_single_card_ask(card1, card2, index1, index2, next_card_number)
            json_requests.append(chat.prompt_as_API_request(prompt, f"cards-{index1}-{index2}"))

    import json
    part_size = len(json_requests) // break_into
    for i in range(break_into):
        with open(f'{output_filename}_part_{i}.jsonl', 'w') as outfile:
            start = i*part_size
            end = ((i+1)*part_size) if (i+1) < break_into else len(json_requests)
            partition = json_requests[start:end]
            for entry in partition:
                json.dump(entry, outfile)
                outfile.write('\n')
        
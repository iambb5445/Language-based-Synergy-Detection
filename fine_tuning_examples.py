from utility import TextUtil
from sts_prompts import SYNERGY_KEYWORD, SYNERGY_KEYWORD_CAPITALIZED,\
    SYNERGY_KEYWORD_PLURAL, SYNERGY_KEYWORD_VERB

examples = [
    #34, 17, 62, 6; 68, 65, 44, 6
    {
        "X_indices": [34, 17, 62, 6],
        "Y_indices": [68, 65, 6, 44],
        "BundledAnswer": TextUtil.dedent(
            f"""# Case 1
            ### Card Descriptions:
            - **Card 5:**
            - Type: Power
            - Cost: 1
            - Whenever you draw a Status card, draw 1 card.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 5 First:**
            - This card sets up a mechanism that allows you to draw additional cards when Status cards are drawn later.

            - **Playing Card 9 Next:**
            - You exhaust all cards in your hand. Card 5 would still be active.
            - You deal damage based on the number of cards you just exhausted. If you have drawn additional cards via Card 5 before playing Card 9, those will also be exhausted and counted towards the damage calculation.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 5 can result in drawing additional cards. Having more cards in your hand when Card 9 is played enhances its effect.
            - Card 9 exhasts all the cards in your hand, including any Status cards. The means that there will be fewer Status cards in your deck, reducing the continued effectiveness of Card 5 on later turns, because Card 5 effect is permanent.

            ### Conclusion:
            While this {SYNERGY_KEYWORD} has both a negative and positive effect, the positive effect is immediate which makes it more valuable.

            Final score:
            1
            ---NEXT---
            # Case 2
            ### Card Descriptions:
            - **Card 5:**
            - Type: Power
            - Cost: 1
            - Whenever you draw a Status card, draw 1 card.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain the ability to draw an additional card if you draw Status cards from this point on.

            - **Playing Card 10 Next:**
            - The next Attack card you play this turn will be played twice. If you have drawn additional cards via Card 5 before playing Card 10, there may be more Attack cards in your hand that you could play and have it be played twice because of Card 10.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The effectiveness of Card 10 is very sensitive to what Attack card is played after Card 10 that turn. Having Card 5 in play potentially leads to more draws, giving you more options for cards to play.

            ### Conclusion:
            There is small positive indirect {SYNERGY_KEYWORD} between the two cards, since playing Card 5 can result in having more options for what Attack is played twice through Card 10's effect.

            Final score:
            1
            ---NEXT---
            # Case 3
            ### Card Descriptions:
            - **Card 5:**
            - Type: Power
            - Cost: 1
            - Whenever you draw a Status card, draw 1 card.

            - **Card 8:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 5 First:**
            - Sets an ongoing effect to draw additional cards if Status cards are drawn.

            - **Playing Card 8 Next:**
            - Card 8's conditions require that all cards in your hand must be Attacks. Since Card 5 is in play, it makes drawing a Status card more obstructive to Card 8's requirement, since any Status card drawn will trigger Card 5's effect, drawing an additional card which can be a non-Attack card.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Playing Card 5 first can create a scenario where Card 8 cannot be played.
            - As such, there’s a disadvantage from the combination, since the inclusion of Card 5 may block the play of Card 8.

            ### Conclusion:
            The sequence produces a negative effect, as Card 5 inadvertently prevents Card 8 from being played.

            Final score:
            -1
            ---NEXT---
            # Case 4
            ### Card Descriptions:
            - **Card 5:**
            - Type: Power
            - Cost: 1
            - Whenever you draw a Status card, draw 1 card.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - Add 2 Wounds to your hand. Gain 15 Block.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain the effect of drawing an additional card when any Status card is drawn.

            - **Playing Card 11 Next:**
            - You add 2 Wounds to your hand, which are Status cards, and gain 15 Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - By playing Card 11, you add Status cards to your hand that will end up in your deck and can be drawn later.
            - Since Card 5 has a permanent effect, whenever one of these Wound cards are drawn, you will draw  an additional card which would not have happened without Card 5 or 11 being played.

            ### Conclusion:
            Playing these cards leads to a positive {SYNERGY_KEYWORD}, as drawing Wounds allows you to trigger Card 5’s ability to draw more cards.

            Final score:
            1
            ---NEXT---
            # Case 5
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 3 damage 3 times applied to a random enemies each time, possibly hitting the same enemy more than once.

            - **Playing Card 9 Next:**
            - You exhaust all the cards in your hand, dealing damage based on how many cards were exhausted.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - When playing Card 9, Card 6 may or may not be in your hand. However, the effect of Card 6 has no unique impact on the effect of Card 9.

            ### Conclusion:
            There is no positive or negative {SYNERGY_KEYWORD} between Card 6 and Card 9.

            Final score:
            0
            ---NEXT---
            # Case 6
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 3 damage 3 times applied to a random enemies each time, possibly hitting the same enemy more than once.

            - **Playing Card 10 Next:**
            - By playing Card 10, the next Attack card you play this turn is played twice. If you play an Attack card this turn, this can enhance your turn but does not apply retroactively.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 10 does not benefit from Card 6 since Card 6 resolves its effects before Card 10 is played.

            ### Conclusion:
            No positive or negative {SYNERGY_KEYWORD} emerges from this sequence; these card do not interact when played in this order.

            Final score:
            0
            ---NEXT---
            # Case 7
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            - **Card 8:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 3 damage 3 times applied to a random enemies each time, possibly hitting the same enemy more than once.

            - **Playing Card 8 Next:**
            - Card 8 can be played if all cards in your hand are Attack cards. Playing Card 6 does not impact this condition in any way.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There is no effect on the ability to play Card 8 from playing Card 6.

            ### Conclusion:
            This sequence results in a no {SYNERGY_KEYWORD} since Card 6 wouldn't disqualify Card 8 from being played.

            Final score:
            0
            ---NEXT---
            # Case 8
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - Add 2 Wounds to your hand. Gain 15 Block.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 3 damage 3 times applied to a random enemies each time, possibly hitting the same enemy more than once.

            - **Playing Card 11 Next:**
            - You add Wounds to your hand and gain Block. This is not impacted by Card 6’s output.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There is no direct {SYNERGY_KEYWORD} between the two cards as played since the damage effect of Card 6 cannot be improved by playing Card 11 afterwards.
            - Playing Card 6 also does not influence the effect of Card 11 in any way.

            ### Conclusion:
            Overall, while Card 6 has its own benefit, it doesn’t create any meaningful {SYNERGY_KEYWORD} or advantage for Card 11. Thus, there is no direct {SYNERGY_KEYWORD} between them.

            Final score:
            0
            ---NEXT---
            # Case 9
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 7 First:**
            - From your next turn onward, at the start of each turn you will lose 1 HP and draw a card.

            - **Playing Card 9 Next:**
            - You exhaust all cards in your hand and deal damage based on the number of cards exhausted.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The energy or HP loss is not relevant in terms of any benefits gained from Card 9 directly.
            - However, the additional card drawn can enhance the effect of Card 9 since Card 9's effect is proportional to the number of cards in your hand.

            ### Conclusion:
            Playing these two cards in this order leads to a positive {SYNERGY_KEYWORD} since Card 9's effect is enhanced when there are more cards in your hand.

            Final score:
            1
            ---NEXT---
            # Case 10
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            ### Order of Events
            - **Playing Card 7 First:**
            - From your next turn onward, at the start of each turn you will lose 1 HP and draw a card.

            - **Playing Card 10 Next:**
            - This card is played to set your next Attack this turn to be played twice for whatever cards exist in hand or drawn (if it's an Attack card).

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Having Card 7 in play leads to more cards drawn on future turns, but not this turn.
            - If Card 10 is played on a future turn, there will be more cards in your hand, some of which can be Attack cards. Because of this, there can be more options to choose from for Card 10 to affect.

            ### Conclusion:
            There is a positive {SYNERGY_KEYWORD} effect when these cards are played in this particular order since Card 7's effect can result in having more options for what Attack is played twice.

            Final score:
            1
            ---NEXT---
            # Case 11
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            - **Card 8:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 7 First:**
            - From your next turn onward, at the start of each turn you will lose 1 HP and draw a card.

            - **Playing Card 8 Next:**
            - If drawing more Cards leads to having non-Attack cards, you can potentially be prevented from playing Card 8 since it relies on the condition of not holding any cards not labeled as Attack cards.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - If you hold non-Attack cards, it blocks Card 8. This results in a potential detriment if Card 7 causes you to draw such a card.

            ### Conclusion:
            There is a negative {SYNERGY_KEYWORD} since the ability to play Card 8 hinges on what cards you have in your hand . Playing Card 7 creates the possibility of drawing a non-Attack card—hence creating a negative {SYNERGY_KEYWORD}.

            Final score:
            -1
            ---NEXT---
            # Case 12
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - Add 2 Wounds to your hand. Gain 15 Block.

            ### Order of Events
            - **Playing Card 7 First:**
            - From your next turn onward, at the start of each turn you will lose 1 HP and draw a card.

            - **Playing Card 11 Next:**
            - You add 2 Wounds (Status cards) to your hand and gain 15 Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The negative effect of adding Wounds from Card 11 directly hinders the positive effect of drawing an additional card each turn gained from Card 7, since the drawn cards now can be Wounds.
            - The positive effect of drawing an additional card each turn gained from Card 7 directly counteracts the negative effect of having your deck diluted with Wounds from Card 11.

            ### Conclusion:
            Given this {SYNERGY_KEYWORD} has both a positive and negative side and these sides are relatively balanced, we can consider this as having no significant {SYNERGY_KEYWORD}.

            Final score:
            0
            ---NEXT---
            # Case 13
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 8 First:**
            - This card is played, assuming that there are no non-Attack cards in your hand, dealing 14 damage.

            - **Playing Card 9 Next:**
            - When this card is played, all cards in your hand are exhausted and damage proportional to the number of cards exhausted is dealt to an enemy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - By playing Card 8, you deal 14 damage to an enemy.
            - Card 9 does not gain or lose effectiveness as a result of playing Card 8.

            ### Conclusion:
            Card 8 serves as a solid Attack, following it with Card 9 has no additional positive or negative {SYNERGY_KEYWORD}.

            Final score:
            0
            ---NEXT---
            # Case 14
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            ### Order of Events
            - **Playing Card 8 First:**
            - This card would deal 14 damage since it gets played first.

            - **Playing Card 10 Next:**
            - Playing Card 10 sets you up to play your next Attack this turn twice.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - You have to consider that playing Card 10 after Card 8 doesn’t retroactively allow Card 8 to be played again and benefit.
            - Playing Card 8 does not influence future attacks played with Card 10.

            ### Conclusion:
            As both cards operate independently, the effects do not generate a {SYNERGY_KEYWORD} leading to a specific outcome.

            Final score:
            0
            ---NEXT---
            # Case 15
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 8 First:**
            - Assuming the conditions are met, you can play this card, dealing 14 damage.

            - **Playing Card 8 Next:**
            - Assuming the conditions are met again when another one of this card is played, you can deal 14 damage again.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Given that these cards do not enhance each other's effect or make the requirement for playing Card 8 more or less likely, there is no {SYNERGY_KEYWORD} between the two cards.

            ### Conclusion:
            There is no positive or negative {SYNERGY_KEYWORD} between the two cards.

            Final score:
            0
            ---NEXT---
            # Case 16
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - Add 2 Wounds to your hand. Gain 15 Block.

            ### Order of Events
            - **Playing Card 8 First:**
            - Assuming all cards are Attack cards, deal 14 damage.

            - **Playing Card 11 Next:**
            - Add Status cards (Wounds) to your hand which disrupts the potential to play another card from Card 8 if applicable.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Playing Card 11 after Card 8 would reduce your capability to play Card 8 in the future.
            - However, for the purposes of the {SYNERGY_KEYWORD} between these cards in this order, playing Card 8 would have no effect on playing Card 11, and the future plays of Card 8 are irrelevant.

            ### Conclusion:
            Since Card 11 would not retroactively stop you from playing Card 8, there is no {SYNERGY_KEYWORD}.

            Final score:
            0""")
    },
    # 4, 38, 44, 59; 5, 33, 43, 59
    {
        "X_indices": [4, 38, 44, 59],
        "Y_indices": [5, 33, 43, 59],
        "BundledAnswer": TextUtil.dedent(f"""# Case 1
            ### Card Descriptions:
            - **Card 5:** 
            - Type: Skill
            - Cost: 1
            - Gain 5 Block. Upgrade a card in your hand for the rest of combat.

            - **Card 9:** 
            - Type: Attack
            - Cost: 1
            - Deal damage equal to your current Block.

            ### Order of Events
            - **Playing Card 5 First:** 
            - You gain 5 Block.

            - **Playing Card 9 Next:** 
            - Deals damage equal to your current Block (5), resulting in 5 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage from Card 9 is reliant on the Block provided by Card 5. Without Card 5, Card 9 would deal no damage.
            
            ### Conclusion:
            This sequence demonstrates a positive {SYNERGY_KEYWORD}, as Card 5 increases the functionality of Card 9 by enabling it to deal damage.

            Final score:
            1
            ---NEXT---
            # Case 2
            ### Card Descriptions:
            - **Card 5:** 
            - Type: Skill
            - Cost: 1
            - Gain 5 Block. Upgrade a card in your hand for the rest of combat.

            - **Card 10:** 
            - Type: Skill
            - Cost: 2
            - Double your current Block.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 5 Block.
            
            - **Playing Card 10 Next:**
            - Doubles the Block from 5 to 10 Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - This showcases a very effective {SYNERGY_KEYWORD}. The initial Block from Card 5 enhances the benefit from Card 10 by providing a solid base to double.

            ### Conclusion:
            A strong {SYNERGY_KEYWORD} from the combination is clearly evident in the increased Block value.

            Final score:
            1
            ---NEXT---
            # Case 3
            ### Card Descriptions:
            - **Card 5:** 
            - Type: Skill
            - Cost: 1
            - Gain 5 Block. Upgrade a card in your hand for the rest of combat.

            - **Card 11:** 
            - Type: Power
            - Cost: 1
            - At the end of your turn, gain 3 Block.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 5 Block.

            - **Playing Card 11 Next:**
            - At the end of your turn, gain an additional 3 Block, for a total of 8 Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - While both cards contribute positively to Block totals, the interaction remains relatively standard and lacks further productive {SYNERGY_KEYWORD} beyond their individual effects.

            ### Conclusion:
            The total Block is increased but does not yield extraordinary outcomes due to lack of deeper interaction between both cards.

            Final score:
            0
            ---NEXT---
            # Case 4
            ### Card Descriptions:
            - **Card 5:** 
            - Type: Skill
            - Cost: 1
            - Gain 5 Block. Upgrade a card in your hand for the rest of combat.

            - **Card 8:** 
            - Type: Power
            - Cost: 3
            - Block is not removed at the start of your turn.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 5 Block.

            - **Playing Card 8 Next:**
            - This means your Block will persist into the next turn.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The ability to carry Over the Block ensures solid defensive capabilities going into future rounds, establishing beneficial resilience.

            ### Conclusion:
            This sequence reflects positive {SYNERGY_KEYWORD} for long-term block buildup.

            Final score:
            1
            ---NEXT---
            # Case 5
            ### Card Descriptions:
            - **Card 6:** 
            - Type: Skill
            - Cost: 1
            - Ethereal. Gain 10 Block.

            - **Card 9:** 
            - Type: Attack
            - Cost: 1
            - Deal damage equal to your current Block.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 10 Block.
            
            - **Playing Card 9 Next:**
            - This deals damage equal to the current Block (10), resulting in 10 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage from Card 9 directly corresponds to the Block gained from Card 6, demonstrating clear {SYNERGY_KEYWORD} by maximizing damage output based on accrued Block.

            ### Conclusion:
            This interaction is positive {SYNERGY_KEYWORD} as it utilizes the Block gain to initiate potential damage.

            Final score:
            1
            ---NEXT---
            # Case 6
            ### Card Descriptions:
            - **Card 6:** 
            - Type: Skill
            - Cost: 1
            - Ethereal. Gain 10 Block.

            - **Card 10:** 
            - Type: Skill
            - Cost: 2
            - Double your current Block.

            ### Order of Events
            - **Playing Card 6 First:** 
            - You gain 10 Block.

            - **Playing Card 10 Next:**
            - Doubles that Block to 20.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - This sequence demonstrates excellent {SYNERGY_KEYWORD}, doubling your current Block to amplify defensive capabilities significantly.

            ### Conclusion:
            The strong {SYNERGY_KEYWORD} results in a high degree of effectiveness through maximizing Block application.

            Final score:
            1
            ---NEXT---
            # Case 7
            ### Card Descriptions:
            - **Card 6:** 
            - Type: Skill
            - Cost: 1
            - Ethereal. Gain 10 Block.

            - **Card 11:** 
            - Type: Power
            - Cost: 1
            - At the end of your turn, gain 3 Block.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 10 Block.

            - **Playing Card 11 Next:**
            - This adds an extra 3 Block at the end of the turn, resulting in 13 Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Though the total Block is respectable, the effect of Card 11 does not derive additional {SYNERGY_KEYWORD} from Card 6 directly.

            ### Conclusion:
            The combination boosts total Block, but lacks deeper interaction between the plays.

            Final score:
            0
            ---NEXT---
            # Case 8
            ### Card Descriptions:
            - **Card 6:** 
            - Type: Skill
            - Cost: 1
            - Ethereal. Gain 10 Block.

            - **Card 8:** 
            - Type: Power
            - Cost: 3
            - Block is not removed at the start of your turn.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 10 Block.

            - **Playing Card 8 Next:**
            - Ensures that Block is retained for the next turn.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Retaining 10 Block for next turn creates a strategic advantage for future plays, demonstrating a good {SYNERGY_KEYWORD}.

            ### Conclusion:
            This sequence is effective due to the combination of immediate and future Block retention.

            Final score:
            1
            ---NEXT---
            # Case 9
            ### Card Descriptions:
            - **Card 7:** 
            - Type: Skill
            - Cost: 1
            - Add 2 Wounds to your hand. Gain 15 Block.

            - **Card 9:** 
            - Type: Attack
            - Cost: 1
            - Deal damage equal to your current Block.

            ### Order of Events
            - **Playing Card 7 First:**
            - You gain 15 Block and add 2 Wounds to your hand.

            - **Playing Card 9 Next:**
            - Deals damage equal to your current Block (15), resulting in 15 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage is effectively realized due to the Block gained from Card 7. The Wounds added don't contribute to this interaction.

            ### Conclusion:
            This pair has a positive {SYNERGY_KEYWORD} with respect to damage scaling based on Block.

            Final score:
            1
            ---NEXT---
            # Case 10
            ### Card Descriptions:
            - **Card 7:** 
            - Type: Skill
            - Cost: 1
            - Add 2 Wounds to your hand. Gain 15 Block.

            - **Card 10:** 
            - Type: Skill
            - Cost: 2
            - Double your current Block.

            ### Order of Events
            - **Playing Card 7 First:**
            - You gain 15 Block and add 2 Wounds to your hand.

            - **Playing Card 10 Next:**
            - Doubles the Block to 30.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Doubling the initial Block gained from Card 7 signifies a robust outcome with benefits extracted from both cards effectively.

            ### Conclusion:
            The combination clearly exhibits positive {SYNERGY_KEYWORD} by leveraging Block enhancement.

            Final score:
            1
            ---NEXT---
            # Case 11
            ### Card Descriptions:
            - **Card 7:** 
            - Type: Skill
            - Cost: 1
            - Add 2 Wounds to your hand. Gain 15 Block.

            - **Card 11:** 
            - Type: Power
            - Cost: 1
            - At the end of your turn, gain 3 Block.

            ### Order of Events
            - **Playing Card 7 First:**
            - You gain 15 Block and 2 Wounds.

            - **Playing Card 11 Next:**
            - Provides an extra 3 Block at the turn's end, totaling 18 Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Although the total Block is beneficial, the wounds do not enhance the effects positively.

            ### Conclusion:
            The interaction produces a straightforward Block gain without significant intra-card {SYNERGY_KEYWORD}.

            Final score:
            0
            ---NEXT---
            # Case 12
            ### Card Descriptions:
            - **Card 7:** 
            - Type: Skill
            - Cost: 1
            - Add 2 Wounds to your hand. Gain 15 Block.


            - **Card 8:** 
            - Type: Power
            - Cost: 3
            - Block is not removed at the start of your turn.

            ### Order of Events
            - **Playing Card 7 First:**
            - You gain 15 Block and add 2 Wounds.

            - **Playing Card 8 Next:**
            - Ensures that the 15 Block stays through the next turn.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - This strategic pairing provides strong defensive strategies for future turns, indicating higher efficacy.

            ### Conclusion:
            This sequence demonstrates positive {SYNERGY_KEYWORD} through Block retention in subsequent turns.

            Final score:
            1
            ---NEXT---
            # Case 13
            ### Card Descriptions:
            - **Card 8:** 
            - Type: Power
            - Cost: 3
            - Block is not removed at the start of your turn.

            - **Card 9:** 
            - Type: Attack
            - Cost: 1
            - Deal damage equal to your current Block.

            ### Order of Events
            - **Playing Card 8 First:**
            - Block is retained for the next turn.
            
            - **Playing Card 9 Next:**
            - Deals damage equal to the current Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - It showcases good use of Block retention for damage, as any block gained inbetween makes Card 9 stronger because of Card 8 being played.

            ### Conclusion:
            This results in a positive {SYNERGY_KEYWORD} as the damage can grow a lot.

            Final score:
            1
            ---NEXT---
            # Case 14
            ### Card Descriptions:
            - **Card 8:** 
            - Type: Power
            - Cost: 3
            - Block is not removed at the start of your turn.

            - **Card 10:** 
            - Type: Skill
            - Cost: 2
            - Double your current Block.

            ### Order of Events
            - **Playing Card 8 First:**
            - Retains Block for the next round.

            - **Playing Card 10 Next:**
            - Doubles the Block amount.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The pairing is extremely effective, ensuring the retained Block is subsequently maximized.

            ### Conclusion:
            This sequence exhibits strong positive {SYNERGY_KEYWORD} through effective interaction between cards.

            Final score:
            1
            ---NEXT---
            # Case 15
            ### Card Descriptions:
            - **Card 8:** 
            - Type: Power
            - Cost: 3
            - Block is not removed at the start of your turn.

            - **Card 11:** 
            - Type: Power
            - Cost: 1
            - At the end of your turn, gain 3 Block.

            ### Order of Events
            - **Playing Card 8 First:**
            - Retains Block into the next turn.

            - **Playing Card 11 Next:**
            - Adds additional 3 Block at the end.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The effective production of Block results in a steady buildup of block that can be cached in when you take damage.

            ### Conclusion:
            This interaction produces a strong {SYNERGY_KEYWORD} through heightened Block totals.

            Final score:
            1
            ---NEXT---
            # Case 16
            ### Card Descriptions:
            - **Card 8:** 
            - Type: Power
            - Cost: 3
            - Block is not removed at the start of your turn.

            ### Order of Events
            - **Playing Card 8 First:** 
            - You maintain the current Block and the Block from future plays.

            - **Playing Another Card 8 Next:** 
            - Does nothing since the block is already maintined

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - While Card 8 is a good card in its own right, it has no extra effect when played with another Card 8.
            - Instead of getting the effect of first card (Card 8) plus second card (the second Card 8), we only get effect of one Card 8.
            - There is a difference in the effect that we get from playing these two cards together in one run compared to the effect of playing one plus the effect of playing the other.
            
            ### Conclusion:
            The engagement demonstrates negative {SYNERGY_KEYWORD} through playing the second Card 8 because the effect has lessened compared to adding the effect of the two together.

            Final score:
            -1""")
    },
    #15, 19, 63, 73; 25, 32, 52, 73
    {
        "X_indices": [15, 19, 63, 73],
        "Y_indices": [25, 32, 52, 73],
        "BundledAnswer": TextUtil.dedent(
            f"""# Case 1
            ### Card Descriptions:
            - **Card 5:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Draw 1 card.

            - **Card 9:**
            - Type: Skill
            - Cost: 0
            - Lose 3 HP. Gain 2 energy.

            ### Order of Events
            - **Playing Card 5 First:**
            - You deal 9 damage to an enemy and draw 1 card.

            - **Playing Card 9 Next:**
            - You lose 3 HP, gain 2 energy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage dealt and card draw from Card 5 does not interact with the subsequent effects of Card 9.
            - There's added {SYNERGY_KEYWORD} between these two cards in their combination — since Card 5 gives you more options and Card 9 gives more energy to pick from your expanded options.

            ### Conclusion:
            The combination of these two cards produces an advantageous effect.

            Final score:
            1
            ---NEXT---
            # Case 2
            ### Card Descriptions:
            - **Card 5:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Draw 1 card.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Create a copy of an Attack or Power card in your hand.

            ### Order of Events
            - **Playing Card 5 First:**
            - You deal 9 damage to an enemy and draw 1 card.

            - **Playing Card 10 Next:**
            - You copy a different Attack or Power card if drawn.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 5 allows for drawing a card that could potentially be used with Card 10, giving you more options of what card to copy.

            ### Conclusion:
            Playing Card 5 first provides a direct advantage of drawing another card to use for the effect of Card 10.

            Final score:
            1
            ---NEXT---
            # Case 3
            ### Card Descriptions:
            - **Card 5:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Draw 1 card.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            ### Order of Events
            - **Playing Card 5 First:**
            - You deal 9 damage and draw a card.

            - **Playing Card 11 Next:**
            - You gain 2 energy but exhaust Card 11.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The order does not specifically enhance or reduce effects compared to playing them separately.
            - Yet as you gain energy from Card 11, as Card 5 gives you more options, you can now more cards to play pick from your expanded options

            ### Conclusion:
            There is no a {SYNERGY_KEYWORD} in the play order between Card 5 and Card 11. The energy gain ehances the draw reaped from Card 5’s play.

            Final score:
            1
            ---NEXT---
            # Case 4
            ### Card Descriptions:
            - **Card 5:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Draw 1 card.

            - **Card 8:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            ### Order of Events
            - **Playing Card 5 First:**
            - You deal 9 damage and draw 1 card.

            - **Playing Card 8 Next:**
            - You lose 6 HP, gain 2 energy, and draw 3 more cards. The card then exhausts.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The order does not specifically enhance or reduce effects compared to playing them separately.
            - While you gain energy from Card 8, the two card effects operate independently and do not create any chain reaction of {SYNERGY_KEYWORD} from the order.

            ### Conclusion:
            There is no direct {SYNERGY_KEYWORD} in the play order between Card 5 and Card 8.

            Final score:
            0
            ---NEXT---
            # Case 5
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - Gain 7 Block. Exhaust a random card from your hand.

            - **Card 9:**
            - Type: Skill
            - Cost: 0
            - Lose 3 HP. Gain 2 energy.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 7 Block but exhaust a random card.

            - **Playing Card 9 Next:**
            - You lose 3 HP and gain 2 energy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The only interaction occurs through the HP loss after gaining Block, where you will end up reducing your effective HP and might lean toward utilizing the Block received from Card 6 to cover for the damage.
            - Despite the sequence order, the two cards do not positively enhance one another’s effects.

            ### Conclusion:
            Neither card significantly augments the outcome of the other, promoting independent function rather than {SYNERGY_KEYWORD}.

            Final score:
            0
            ---NEXT---
            # Case 6
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - Gain 7 Block. Exhaust a random card from your hand.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Create a copy of an Attack or Power card in your hand.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 7 Block, exhausting a random card.

            - **Playing Card 10 Next:**
            - You create a copy of an Attack or Power card in your hand.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The interplay between these two cards is minimal. While Card 6 provides protective Block, it does not specifically interact with Card 10’s ability to copy an Attack or Power card.
            - There’s no distinct advantage or iterative relationship to the combination.

            ### Conclusion:
            The effect of Block from Card 6 does not enhance or restrict the utility gained from playing Card 10. Each card serves an individual purpose rather than combine for added benefit.

            Final score:
            0
            ---NEXT---
            # Case 7
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - Gain 7 Block. Exhaust a random card from your hand.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 7 Block while exhausting a random card.

            - **Playing Card 11 Next:**
            - You gain 2 energy but exhaust Card 11.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The effects from each card do not lead into one another in terms of {SYNERGY_KEYWORD} or augmented outcomes. While the Block is an attempt to secure HP, gaining energy does not have any added effect as the two processes operate independently.

            ### Conclusion:
            Their individual impacts don’t produce a unique outcome that improves or adversely affects the effect of the other in terms of {SYNERGY_KEYWORD}, leading to an independent result.

            Final score:
            0
            ---NEXT---
            # Case 8
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - Gain 7 Block. Exhaust a random card from your hand.

            - **Card 8:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 7 Block and exhaust a random card.

            - **Playing Card 8 Next:**
            - You lose 6 HP, gain 2 energy, and draw 3 cards.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The only interaction occurs through the HP loss after gaining Block, where you will end up reducing your effective HP and might lean toward utilizing the Block received from Card 6 to cover for the damage.
            - Despite the sequence order, the two cards do not positively enhance one another’s effects. 

            ### Conclusion:
            Neither card significantly augments the outcome of the other, promoting independent function rather than {SYNERGY_KEYWORD}.

            Final score:
            0
            ---NEXT---
            # Case 9
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 3
            - Skills cost 0. Whenever you play a Skill, Exhaust it.

            - **Card 9:**
            - Type: Skill
            - Cost: 0
            - Lose 3 HP. Gain 2 energy.

            ### Order of Events
            - **Playing Card 7 First:**
            - Skills cost 0 now and subsequently exhausting the skills played.

            - **Playing Card 9 Next:**
            - Lose 3 HP and gain 2 energy, due to it being a Skill, it is exhausted.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - After playing Card 7, it allows you to utilize Card 9 without energy cost, activating the effect while having it exhaust automatically.
            - The problem is that Card 9 already cost 0, meaning that all Card 7 did was exhaust Card 9.

            ### Conclusion:
            This combination promotes a negative interaction by eliminating the skill card while discounting you no energy.

            Final score:
            -1
            ---NEXT---
            # Case 10
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 3
            - Skills cost 0. Whenever you play a Skill, Exhaust it.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Create a copy of an Attack or Power card in your hand.

            ### Order of Events
            - **Playing Card 7 First:**
            - Skills now cost 0 and exhausting skills played.

            - **Playing Card 10 Next:**
            - Create a copy of an Attack or Power card.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - While playing Card 10 creates additional cards, the cost reduction from Card 7 allowes you to have more energy in the future for the copied cards.

            ### Conclusion:
            The sequence provides advantages, and despite exhausting Card 10, is a net positive {SYNERGY_KEYWORD}.

            Final score:
            1
            ---NEXT---
            # Case 11
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 3
            - Skills cost 0. Whenever you play a Skill, Exhaust it.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            ### Order of Events
            - **Playing Card 7 First:**
            - Skills now cost 0 and will be exhausted upon use.

            - **Playing Card 11 Next:**
            - Gain 2 energy by playing the skill, which gets exhausted.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The utility observed is primarily a capacity gain which benefits from having free energy with no cost. 
            - Using it provides a deeper tactical option while exhausting the card that was already getting exhusted.

            ### Conclusion:
            The two cards manage to cooperate effectively, allowing for additional energy gain.

            Final score:
            1
            ---NEXT---
            # Case 12
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 3
            - Skills cost 0. Whenever you play a Skill, Exhaust it.

            - **Card 8:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            ### Order of Events
            - **Playing Card 7 First:**
            - Skills cost 0 and exhaust thereafter.

            - **Playing Card 8 Next:**
            - You lose 6 HP, gain 2 energy, and draw 3 cards. It then is exhausted.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Using Card 7 before Card 8 does not have any negatives, as Card 8 is exhausted on being played regardless.
            - The ability to play Card 8 without energy charges is pointless since it costs 0 anyway.

            ### Conclusion:
            The sequence leads to effectively no returns, as both the positve and negative effects of Card 7 are already present in Card 8.

            Final score:
            0
            ---NEXT---
            # Case 13
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            - **Card 9:**
            - Type: Skill
            - Cost: 0
            - Lose 3 HP. Gain 2 energy.

            ### Order of Events
            - **Playing Card 8 First:**
            - Lose 6 HP, gain 2 energy, draw 3 cards, exhaust it.

            - **Playing Card 9 Next:**
            - Lose an additional 3 HP but gain 2 energy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The combination incentivizes energy management and allows you to draw more available cards post the HP loss.

            ### Conclusion:
            Though both cards make you lose HP, the first card provides energy that could be useful in playing cards drawn from Card 9, so they end up impacting eachother, causing a {SYNERGY_KEYWORD}.

            Final score:
            1
            ---NEXT---
            # Case 14
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Create a copy of an Attack or Power card in your hand.

            ### Order of Events
            - **Playing Card 8 First:**
            - Lose 6 HP. Gain 2 energy and draw 3 cards.

            - **Playing Card 10 Next:**
            - Create a copy of an Attack or Power card.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - By drawing 3 cards through Card 8, it allows the player to have alternatives available to copy with Card 10.
            - While Card 10 can create beneficial copies, the energy gain offered through the first play does not specifically tie itself into your {SYNERGY_KEYWORD} pathway moving forward.

            ### Conclusion:
            There’s a connection in terms of potentially getting a card to utilize with Card 10.

            Final score:
            1
            ---NEXT---
            # Case 15
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            ### Order of Events
            - **Playing Card 8 First:**
            - Lose 6 HP, gain 2 energy, draw 3 cards. Exhaust Card 8.

            - **Playing Card 11 Next:**
            - Gain an additional 2 energy, exhausting Card 11.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Playing Card 8 already provides the player with 2 energy while drawing 3 cards, and then playing Card 11 allows for an additional energy gain at the cost of exhausting the card.

            ### Conclusion:
            Each of the effects occurs in isolation, yet since Card 8 gives you more options and Card 11 gives more energy to pick from your expanded options, the have a {SYNERGY_KEYWORD}.

            Final score:
            1
            ---NEXT---
            # Case 16
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            ### Order of Events
            - **Playing Card 8 First:**
            - You lose 6 HP, gain 2 energy, and draw 3 cards before exhausting it.

            - **Playing Card 8 Next:**
            - You lose 6 HP, gain 2 energy, and draw 3 additional cards before exhausting it.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Repeating the action results in an added stack of energy gain and card draw recursively. The downside is accrued HP loss.

            ### Conclusion:
            Although you're losing HP, gaining more energy and cards allows for many extra options and played cards since the energy and crad draw is beneficial to each cards effect, meaning there is a {SYNERGY_KEYWORD}.

            Final score:
            1""")
    },
    # 56, 64, 65, 72; 10, 40, 54, 68
    {
        "X_indices": [56, 64, 65, 72],
        "Y_indices": [10, 40, 54, 68],
        "BundledAnswer": TextUtil.dedent(
            f"""# Case 1
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - If the enemy intends to attack, gain 4 Strength.

            - **Card 9:**
            - Type: Skill
            - Cost: 1
            - Play the top card of your draw pile and Exhaust it.

            ### Order of Events
            - **Playing Card 5 First:**
            - If the enemy intends to attack, you gain 4 Strength.

            - **Playing Card 9 Next:**
            - This will play the top card of your draw pile, it gets played at no cost, but it has no direct interaction with Card 5.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There’s no inherent {SYNERGY_KEYWORD} in these two specific cards since the effectiveness of Card 5 depends on the enemy's intention rather than the card's effects.
            - Card 9 simply plays a card from your draw pile without interacting or benefiting from the Strength gained from Card 5 unless the played card itself directly uses strength.

            ### Conclusion:
            This combination creates no specific interaction between Card 5 and Card 9.

            Final score:
            0
            ---NEXT---
            # Case 2
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - If the enemy intends to attack, gain 4 Strength.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Add a random Attack to your hand. It costs 0 this turn. Exhaust.

            ### Order of Events
            - **Playing Card 5 First:**
            - If the enemy intends to attack, gain 4 Strength.

            - **Playing Card 10 Next:**
            - You add a random Attack to your hand and it costs 0 this turn.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The potential {SYNERGY_KEYWORD} here relies on Card 5 increasing your Strength, which enhances your subsequent Attack damage.
            - Playing Card 10 allows you to play an Attack card that can leverage the 4 Strength buff. Knowing the added card is an attack means it will interact with strength, even if the intensity may differ.

            ### Conclusion:
            Card 10 allows for an enhanced attack by leveraging Card 5's effects since Card 10 adds an attack.

            Final score:
            1
            ---NEXT---
            # Case 3
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - If the enemy intends to attack, gain 4 Strength.

            - **Card 11:**
            - Type: Attack
            - Cost: 2
            - Exhaust all non-Attack cards in your hand. Deal 16 damage.

            ### Order of Events
            - **Playing Card 5 First:**
            - If the enemy intends to attack, gain 4 Strength.

            - **Playing Card 11 Next:**
            - This card exhausts all non-Attack cards in your hand and deals 16 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The strength gained from Card 5 enhances the damage dealt by Card 11.

            ### Conclusion:
            There is enhancement in damage from Card 11 based on Card 5's effect, and thus there's a {SYNERGY_KEYWORD} effect.

            Final score:
            1
            ---NEXT---
            # Case 4
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - If the enemy intends to attack, gain 4 Strength.

            - **Card 12:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 5 First:**
            - If the enemy intends to attack, gain 4 Strength.

            - **Playing Card 12 Next:**
            - Exhausts all cards in your hand. Proceeds to deal damage based on the total number of cards exhausted.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The strength from Card 5 enhances the total damage from Card 12. If there are several cards in hand, the total damage can be utilized to benefit from Card 5’s strength buff which indicates that in the event of enemy intending to attack, it could provide an advantageous situation.
            - However, if you only had Card 5 and Card 12, this {SYNERGY_KEYWORD} remains irrelevant since the lack of cards could hinder context.

            ### Conclusion:
            This sequence of playing Card 5 followed by Card 12 directly produces enhanced effective damage per card exhausted. Hence, it presents a positive aspect.

            Final score:
            1
            ---NEXT---
            # Case 5
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 3
            - At the start of each turn, gain 2 Strength.

            - **Card 9:**
            - Type: Skill
            - Cost: 1
            - Play the top card of your draw pile and Exhaust it.

            ### Order of Events
            - **Playing Card 6 First:**
            - You now gain 2 Strength at the beginning of subsequent turns.

            - **Playing Card 9 Next:**
            - You play the top card of your draw pile this turn and exhaust it.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - While Card 6 allows for a longer-term strength gain across multiple turns, Card 9 plays the card without any incremental strength values. There’s no direct interaction causing a 
            {SYNERGY_KEYWORD} effect between the two specific cards as Card 9 does not utilize or benefit from cumulative Strength.

            ### Conclusion:
            There is no effective {SYNERGY_KEYWORD} created by this play order since the strengthening doesn't apply to the immediate effects of Card 9.

            Final score:
            0
            ---NEXT---
            # Case 6
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 3
            - At the start of each turn, gain 2 Strength.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Add a random Attack to your hand. It costs 0 this turn. Exhaust.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 2 Strength over multiple turns.

            - **Playing Card 10 Next:**
            - Add a random Attack to your hand, which costs 0 this turn.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The added Attack can potentially benefit from the strength if later played but the intensity depends on the attack drawn.

            ### Conclusion:
            Despite the randomness of the generated attack, the {SYNERGY_KEYWORD} effect is present.

            Final score:
            1
            ---NEXT---
            # Case 7
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 3
            - At the start of each turn, gain 2 Strength.

            - **Card 11:**
            - Type: Attack
            - Cost: 2
            - Exhaust all non-Attack cards in your hand. Deal 16 damage.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gained benefit from the power played.

            - **Playing Card 11 Next:**
            - This lets you deal 16 damage while exhausting non-Attack cards in your hand.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 11 utilizes any strength gained from Card 6 since its damage output grows with gained strength.

            ### Conclusion:
            There is enhanced {SYNERGY_KEYWORD} effect when playing in the described order.

            Final score:
            1
            ---NEXT---
            # Case 8
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 3
            - At the start of each turn, gain 2 Strength.

            - **Card 12:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain long-term strength benefits.

            - **Playing Card 12 Next:**
            - This card performs damage based on total exhausted cards in hand.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage could be increased from the strength gained should you have other non-attack cards to exhaust beforehand, as the relationship between Card 6 and 12 allows for cumulative strength enhancements directly related to the counts of cards.

            ### Conclusion:
            In total, the {SYNERGY_KEYWORD_PLURAL} may vary in efficacy regarding the count of cards but it’s positive in situations with more exhaust.

            Final score:
            1
            ---NEXT---
            # Case 9
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            - **Card 9:**
            - Type: Skill
            - Cost: 1
            - Play the top card of your draw pile and Exhaust it.

            ### Order of Events
            - **Playing Card 7 First:**
            - The next attack played will be doubled in effectiveness.

            - **Playing Card 9 Next:**
            - The top card from your draw pile is now played.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The card played from the draw pile could be beneficial if it happens to be an attack. If it does not, there’s no extensive interaction at play.
            - The doubling effect depends entirely on whether the top card played from the draw pile is an Attack or not.

            ### Conclusion:
            There’s no guaranteed {SYNERGY_KEYWORD} yielded by this combination unless the arbitrary card played is an Attack.

            Final score:
            0
            ---NEXT---
            # Case 10
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Add a random Attack to your hand. It costs 0 this turn. Exhaust.

            ### Order of Events
            - **Playing Card 7 First:**
            - The next Attack played will be doubled.

            - **Playing Card 10 Next:**
            - You add a random Attack to your hand at no cost this turn.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - If the drawn attack is played as the next action, it can benefit from being played twice.

            ### Conclusion:
            There is positive {SYNERGY_KEYWORD} in getting a doubled random attack since the Card 10 garuntees that Card 7 can be utilized.

            Final score:
            1
            ---NEXT---
            # Case 11
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            - **Card 11:**
            - Type: Attack
            - Cost: 2
            - Exhaust all non-Attack cards in your hand. Deal 16 damage.

            ### Order of Events
            - **Playing Card 7 First:**
            - Next Attack played gets doubled.

            - **Playing Card 11 Next:**
            - This card exhausts all non-Attack cards and deals flat 16 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 11 is an Attack type, so its damage will be doubled due to the play effects of Card 7, resulting in significantly higher damage overall.
            - Additionally, the second time it's played no more cards will be exhausted.

            ### Conclusion:
            This plays out as a positive {SYNERGY_KEYWORD} due to doubling the damage of Card 11 based on the order, leaving favorable outcomes from the play.

            Final score:
            1
            ---NEXT---
            # Case 12
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            - **Card 12:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 7 First:**
            - Your next attack is doubled.

            - **Playing Card 12 Next:**
            - This exhausts all cards in your hand and deals damage based on the count of cards exhausted.
            - If the cards are played back to back, Card 12 is then played a second time because of the effect of Card 7.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The mechanics sit in favor of any attack damage derived from the doubled effects, especially if multiple cards are exhausted creating higher damage outputs.
            - The first time Card 12 is played, some number of cards are exhausted from your hand and the damage dealt is based on the number of these cards.
            - The effect of Card 7 results in the added effect of playing Card 12 a second time.
            - However, since all the cards are exhausted the first time, the doubling doesn't result in any extra damage, as if the second time did not happen.


            ### Conclusion:
            This is no {SYNERGY_KEYWORD} due to the interaction of losing cards through exhaustion, making the copy deal no damage.

            Final score:
            0
            ---NEXT---
            # Case 13
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Double your Strength. Exhaust.

            - **Card 9:**
            - Type: Skill
            - Cost: 1
            - Play the top card of your draw pile and Exhaust it.

            ### Order of Events
            - **Playing Card 8 First:**
            - Your strength is doubled once and then you exhaust this card.

            - **Playing Card 9 Next:**
            - You immediately play the top card of your draw pile.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The doubling of strength does not impact anything played next unless the top card drawn also makes use of strength in its resolution.

            ### Conclusion:
            There is no intrinsic {SYNERGY_KEYWORD} produced by this card combination, since no additional {SYNERGY_KEYWORD} effect occurs solely from the strength doubling unless paired later with an attacker utilizing strength.

            Final score:
            0
            ---NEXT---
            # Case 14
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Double your Strength. Exhaust.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Add a random Attack to your hand. It costs 0 this turn. Exhaust.

            ### Order of Events
            - **Playing Card 8 First:**
            - Doubling of strength occurs immediately before exhausting this card.

            - **Playing Card 10 Next:**
            - Offers a random attack drawn to your hand whose cost is hinging on the draw.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The doubling of strength interacts with the random attack gained from Card 10 to some degree.
            ### Conclusion:
            Since the next random attack card directly utilizes the strength created, this remains a positive {SYNERGY_KEYWORD}.

            Final score:
            1
            ---NEXT---
            # Case 15
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Double your Strength. Exhaust.

            - **Card 11:**
            - Type: Attack
            - Cost: 2
            - Exhaust all non-Attack cards in your hand. Deal 16 damage.

            ### Order of Events
            - **Playing Card 8 First:**
            - Your strength is doubled before exhausting.

            - **Playing Card 11 Next:**
            - This card deals 16 damage while exhausting non-Attack cards.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - As Card 11 provides damage, it leverages the strength gained from Card 8 as the attack is enhanced.

            ### Conclusion:
            Given that the output from Card 8 amplifies Card 11, the numbers lead to positive effects from {SYNERGY_KEYWORD}.

            Final score:
            1
            ---NEXT---
            # Case 16
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Double your Strength. Exhaust.

            - **Card 12:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 8 First:**
            - Strength is doubled with exhaustion ensuing.

            - **Playing Card 12 Next:**
            - It deals damage based on the amount of cards exhausted, including how the strength boosting could bring better cumulative totals through higher numbers resulting.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The effectiveness of this particular {SYNERGY_KEYWORD} would remain consistent as Strength would only apply once to Card 12.

            ### Conclusion:
            This presents a positive {SYNERGY_KEYWORD} since the mechanics allow greater utilization of damage through the buildup of strengthened capabilities.

            Final score:
            1""")
    },
    # 4, 56, 60, 72; 2, 11, 13, 39
    {
        "X_indices": [4, 56, 60, 72],
        "Y_indices": [2, 11, 13, 39],
        "BundledAnswer": TextUtil.dedent(
            f"""# Case 1
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 5 Block. Upgrade a card in your hand for the rest of combat.

            - **Card 9:**
            - Type: Attack
            - Cost: 1
            - Deal 6 damage.

            ### Order of Events
            - **Playing Card 5 First:**
            - Gain 5 Block and upgrade a card in your hand.

            - **Playing Card 9 Next:**
            - Deal 6 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Playing Card 5 first adds some defensive capability through Block. The upgrade aspect doesn’t impact the immediate damage dealt by Card 9.
            - Given card play order, there’s no {SYNERGY_KEYWORD} since neither card directly enhances the other.

            ### Conclusion:
            No defined {SYNERGY_KEYWORD} effect exists here; both cards perform their functions independently.

            Final score:
            0
            ---NEXT---
            # Case 2
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 5 Block. Upgrade a card in your hand for the rest of combat.

            - **Card 10:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Place a card from your discard pile on top of your draw pile.

            ### Order of Events
            - **Playing Card 5 First:**
            - Gain 5 Block and upgrade a card in your hand.

            - **Playing Card 10 Next:**
            - Deal 9 damage and place a card in the draw pile.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The Block gained from Card 5 does not affect the application of Card 10 directly.
            - Upgrading a card may have future benefits, but per card effect order, no immediate {SYNERGY_KEYWORD} emerges.

            ### Conclusion:
            There’s no interaction or additional advantage moving from Card 5 to Card 10 based on play order.

            Final score:
            0
            ---NEXT---
            # Case 3
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 5 Block. Upgrade a card in your hand for the rest of combat.

            - **Card 11:**
            - Type: Attack
            - Cost: 1
            - Gain 5 Block. Deal 5 damage.

            ### Order of Events
            - **Playing Card 5 First:**
            - Gain 5 Block and upgrade a card in your hand.

            - **Playing Card 11 Next:**
            - You gain 5 Block again and deal 5 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The Block from Card 5 and Card 11 stack, resulting in 10 Block total. There is overlapping effects since both provide Block; however, there’s no additional gains made outside of the basic effects.
            - Additionally, niether card makes the other easier to play or utilize.

            ### Conclusion:
            Overall, this creates no {SYNERGY_KEYWORD} despite both gaining Block and enhancing the player’s defensive capabilities.

            Final score:
            0
            ---NEXT---
            # Case 4
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 5 Block. Upgrade a card in your hand for the rest of combat.

            - **Card 12:**
            - Type: Attack
            - Cost: 1
            - Lose 2 HP. Deal 15 damage.

            ### Order of Events
            - **Playing Card 5 First:**
            - Gain 5 Block and upgrade a card in your hand.

            - **Playing Card 12 Next:**
            - This card would lose 2 HP and deal 15 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The Block from Card 5 helps to absorb damage from any potential attack, while Card 12 allows for significant damage output despite taking HP loss.
            - However, there is no direct benefit to Card 12 from Card 5 since it does not change the damage output or HP loss.

            ### Conclusion:
            While defensive capability from Card 5 is helpful with HP management, there is no unique {SYNERGY_KEYWORD} within the context, resulting in no enhanced collaborative effects.

            Final score:
            0
            ---NEXT---
            # Case 5
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - If the enemy intends to attack, gain 4 Strength.

            - **Card 9:**
            - Type: Attack
            - Cost: 1
            - Deal 6 damage.

            ### Order of Events
            - **Playing Card 6 First:**
            - Gain 4 Strength if enemy intends to attack.

            - **Playing Card 9 Next:**
            - Deal 6 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - If played when the enemy attacks, Card 6 would enhance subsequent damage, and since dealing damage occurs after the fact, Card 9 would benefit from the Strength this turn.    

            ### Conclusion:
            There is {SYNERGY_KEYWORD} effect here given the exact card plays. The output from Card 6 impacts the damage of Card 9.

            Final score:
            1
            ---NEXT---
            # Case 6
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - If the enemy intends to attack, gain 4 Strength.

            - **Card 10:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Place a card from your discard pile on top of your draw pile.

            ### Order of Events
            - **Playing Card 6 First:**
            - Gain 4 Strength if the enemy intends to attack.

            - **Playing Card 10 Next:**
            - Deal 9 damage and reorder the top card of your draw pile.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - If you gain Strength from Card 6 due to an enemy action, Card 10’s damage does scale as it takes effect later.

            ### Conclusion:
            There’s {SYNERGY_KEYWORD} observed between Card 6 activating with Card 10; the damage dealt is amplified.

            Final score:
            1
            ---NEXT---
            # Case 7
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - If the enemy intends to attack, gain 4 Strength.

            - **Card 11:**
            - Type: Attack
            - Cost: 1
            - Gain 5 Block. Deal 5 damage.

            ### Order of Events
            - **Playing Card 6 First:**
            - If the enemy intends to attack, gain 4 Strength.

            - **Playing Card 11 Next:**
            - Gain 5 Block and deal 5 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - If realized, the Strength gained from Card 6 would impact how much damage is dealt using Card 11 since it's an attack.

            ### Conclusion:
            Bonus damage occurs between these two cards based on the sequence in which they’re played.

            Final score:
            1
            ---NEXT---
            # Case 8
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - If the enemy intends to attack, gain 4 Strength.

            - **Card 12:**
            - Type: Attack
            - Cost: 1
            - Lose 2 HP. Deal 15 damage.

            ### Order of Events
            - **Playing Card 6 First:**
            - If the enemy intends to attack, gain 4 Strength.

            - **Playing Card 12 Next:**
            - This card loses 2 HP and deals 15 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 6’s effects remain separate from Card 12, but the damage resolves with an increase of 4 from prior plays.

            ### Conclusion:
            This yield's an effective combination bonuses based on the sequence played.

            Final score:
            1
            ---NEXT---
            # Case 9
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 9:**
            - Type: Attack
            - Cost: 1
            - Deal 6 damage.

            ### Order of Events
            - **Playing Card 7 First:**
            - Gain 2 Vulnerable, setting up future attacks to deal more damage.

            - **Playing Card 9 Next:**
            - Deal 6 damage, which is increased to 9 from the vulnerable

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - While Card 9 deals 6 damage, you being Vulnerable doesnt apply to the damage. The energy gain doesn't impact Card 9 either.

            ### Conclusion:
            As it stands, immediate does not benefit exist when considering the combination of Card 7 with Card 9.

            Final score:
            0
            ---NEXT---
            # Case 10
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 10:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Place a card from your discard pile on top of your draw pile.

            ### Order of Events
            - **Playing Card 7 First:**
            - Gain 2 Vulnerable.

            - **Playing Card 10 Next:**
            - Deal 9 damage, not increased by vulnerable, and manipulate the draw pile.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 10 doesn't benefits from Card 7 in this immediate moment, since the vulnerable state gets put on you and not the enemy.

            ### Conclusion:
            There is no advantageous {SYNERGY_KEYWORD} from the play sequence of Card 7 to Card 10.

            Final score:
            0
            ---NEXT---
            # Case 11
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 11:**
            - Type: Attack
            - Cost: 1
            - Gain 5 Block. Deal 5 damage.

            ### Order of Events
            - **Playing Card 7 First:**
            - Gain 2 Vulnerable as a result of the play.

            - **Playing Card 11 Next:**
            - Gain 5 Block and deal 5 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - While gaining 5 Block and dealing damage occurs independently, the gained vulnerability does not help in this sequence.

            ### Conclusion:
            Results indicate that there’s no observable {SYNERGY_KEYWORD} available through the order of card play.

            Final score:
            0
            ---NEXT---
            # Case 12
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 12:**
            - Type: Attack
            - Cost: 1
            - Lose 2 HP. Deal 15 damage.

            ### Order of Events
            - **Playing Card 7 First:**
            - Gain 2 Vulnerable.

            - **Playing Card 12 Next:**
            - This card will lose 2 HP and able to deal 15 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - While 15 damage is substantial, the vulnerability does not affect this outcome, since it is applied to you.

            ### Conclusion:
            {SYNERGY_KEYWORD_CAPITALIZED} is not here as Card 12 performs damage on the enemy, and the vulnerability status is put on you by the prior play.

            Final score:
            0
            ---NEXT---
            # Case 13
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Double your Strength. Exhaust.

            - **Card 9:**
            - Type: Attack
            - Cost: 1
            - Deal 6 damage.

            ### Order of Events
            - **Playing Card 8 First:**
            - Your strength is doubled and this card exhausts.

            - **Playing Card 9 Next:**
            - Deal 6 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The doubling effect alters the damage dealt through Card 9 since it is resolved with benefit from strength.

            ### Conclusion:
            Therefore, a {SYNERGY_KEYWORD} effect is gained between these two cards in this order.

            Final score:
            1
            ---NEXT---
            # Case 14
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Double your Strength. Exhaust.

            - **Card 10:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Place a card from your discard pile on top of your draw pile.

            ### Order of Events
            - **Playing Card 8 First:**
            - Your strength is doubled and then exhausted.

            - **Playing Card 10 Next:**
            - Deal 9 damage and manipulate the draw pile.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Doubling strength occurs preemptively being able to amplify the outcome of Card 10.

            ### Conclusion:
            There’s {SYNERGY_KEYWORD} as the play of Card 10 is enhanced based upon strength established in advance.

            Final score:
            1
            ---NEXT---
            # Case 15
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Double your Strength. Exhaust.

            - **Card 11:**
            - Type: Attack
            - Cost: 1
            - Gain 5 Block. Deal 5 damage.

            ### Order of Events
            - **Playing Card 8 First:**
            - Strength is doubled and the card is exhausted.

            - **Playing Card 11 Next:**
            - This grants 5 Block and deals 5 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The attack damage values change, leveraging the capability from doubling the strength prior to the action being taken.

            ### Conclusion:
            So an added effect is witnessed from the combination of these two card plays leading to a greater {SYNERGY_KEYWORD} being established.

            Final score:
            1
            ---NEXT---
            # Case 16
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Double your Strength. Exhaust.

            - **Card 12:**
            - Type: Attack
            - Cost: 1
            - Lose 2 HP. Deal 15 damage.

            ### Order of Events
            - **Playing Card 8 First:**
            - Strength effectively doubles and is exhausted.

            - **Playing Card 12 Next:**
            - This causes you to lose 2 HP while dealing 15 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage is increased by any previous strength increases times two since Card 12’s an attack.

            ### Conclusion:
            Ultimately, the {SYNERGY_KEYWORD} emerged as Card 12's damage increased.

            Final score:
            1""")
    },
    # 33, 60, 30, 7; 31, 32, 65, 35; 5
    {
        "X_indices": [33, 60, 30, 7],
        "Y_indices": [31, 32, 65, 35],
        "BundledAnswer": TextUtil.dedent(f"""# Case 1
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 2
            - Double your current Block.

            - **Card 9:**
            - Type: Attack
            - Cost: 1
            - Deal 5 damage. If the enemy is Vulnerable, gain 1 energy and draw 1 card.

            ### Order of Events
            - **Playing Card 5 First:**
            - You double your current Block. Let's assume you had X Block before playing, your new Block would be 2X.

            - **Playing Card 9 Next:**
            - Card 9 will deal 5 damage. There is no interaction between doubling Block and the effects of Card 9.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There is no {SYNERGY_KEYWORD} between the two cards. Doubling your Block does not enhance the effectiveness of dealing damage or gaining energy from vulnerabilities since it’s unrelated to the Block played.

            ### Conclusion:
            No additional advantages or disadvantages arise from this sequence.

            Final score:
            0
            ---NEXT---
            # Case 2
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 2
            - Double your current Block.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Create a copy of an Attack or Power card in your hand.

            ### Order of Events
            - **Playing Card 5 First:**
            - You double your current Block.

            - **Playing Card 10 Next:**
            - You create a copy of an Attack or Power card in your hand. Block is unaffected, and Card 10 does not provide {SYNERGY_KEYWORD} with previous effects.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - As Card 10's effect is independent of Card 5, there’s no {SYNERGY_KEYWORD} or interaction between the two cards beyond individual independent effects.

            ### Conclusion:
            No {SYNERGY_KEYWORD} effects or additional advantages exist between these two.

            Final score:
            0
            ---NEXT---
            # Case 3
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 2
            - Double your current Block.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            ### Order of Events
            - **Playing Card 5 First:**
            - You double your current Block.

            - **Playing Card 11 Next:**
            - This creates a buff for the next Attack played but does not interact with the Block gain from Card 5.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The doubling of the Block does not enhance the effect of having an Attack played twice. These two effects are independent from one another.

            ### Conclusion:
            No {SYNERGY_KEYWORD} effect exists between these plays, neither advantageous nor disadvantageous.

            Final score:
            0
            ---NEXT---
            # Case 4
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 2
            - Double your current Block.

            - **Card 12:**
            - Type: Power
            - Cost: 1
            - Whenever a card is Exhausted, gain 3 Block.

            ### Order of Events
            - **Playing Card 5 First:**
            - You double your current Block.

            - **Playing Card 12 Next:**
            - There is no Exhaustion effect taking place, so the effect gets triggered only when an exhaust action follows.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The Block gain from Card 12 happens only on Exhaust actions. Since no {SYNERGY_KEYWORD} exists between the two effects, doubling your Block does not enhance the effect derived from Exhausting cards.

            ### Conclusion:
            No combinatory effect is seen between these plays.

            Final score:
            0
            ---NEXT---
            # Case 5
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 9:**
            - Type: Attack
            - Cost: 1
            - Deal 5 damage. If the enemy is Vulnerable, gain 1 energy and draw 1 card.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 2 Vulnerable.

            - **Playing Card 9 Next:**
            - Card 9 deals 5 damage to the enemy. Since the you are now Vulnerable, not the enemy, nothing else happens.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The {SYNERGY_KEYWORD} here is nonexistent. Playing Card 6 first does not give an enemy vulnerable, which means Card 9 does not trigger the additional effects for energy and card draw.

            ### Conclusion:
            This sequence creates no {SYNERGY_KEYWORD} where playing Card 6 fails to empower Card 9.

            Final score:
            0
            ---NEXT---
            # Case 6
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Create a copy of an Attack or Power card in your hand.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 2 Vulnerable.

            - **Playing Card 10 Next:**
            - You create a copy of an Attack or Power card in your hand, but it does not interact or enhance any existing cards since it’s dependent on what is currently in hand.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 10 can create a copy of existing attacks or power cards, and since you need more energy to play that extra card, Card 6 provides that energy, making them work well off each other.

            ### Conclusion:
            A small additional advantage occurs in this sequence, leading to a small {SYNERGY_KEYWORD}.

            Final score:
            1
            ---NEXT---
            # Case 7
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 2 Vulnerable.

            - **Playing Card 11 Next:**
            - This will allow your next Attack to be played twice that turn.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The increased vulnerability allows for enhanced damage, but only to the player. Any following Attack played twice does not benefit from vulnerability on you.

            ### Conclusion:
            This sequence generates no {SYNERGY_KEYWORD} where Card 11 can not from the increased vulnerability from Card 6 since it is applied to you.

            Final score:
            0
            ---NEXT---
            # Case 8
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 12:**
            - Type: Power
            - Cost: 1
            - Whenever a card is Exhausted, gain 3 Block.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 2 Vulnerable.

            - **Playing Card 12 Next:**
            - You establish a future effect that grants Block whenever a card is Exhausted.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There’s no direct destruction or {SYNERGY_KEYWORD} here. Card 12's effect links to exhaust activity that would normally lead to Block gains, not relevant with the effect of Card 6.

            ### Conclusion:
            No additional {SYNERGY_KEYWORD} interactions are present between these two.

            Final score:
            0
            ---NEXT---
            # Case 9
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - Enemy loses 2 Strength. Exhaust.

            - **Card 9:**
            - Type: Attack
            - Cost: 1
            - Deal 5 damage. If the enemy is Vulnerable, gain 1 energy and draw 1 card.

            ### Order of Events
            - **Playing Card 7 First:**
            - The enemy loses 2 Strength, and the card is then Exhausted.

            - **Playing Card 9 Next:**
            - Card 9 will deal 5 damage. There are no Vulnerable interactions preceding the attack from Card 7 and no further attacks resulting from the effect of Card 7.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The strength loss occurs before dealing damage, but Card 9 does not exploit any of these changes unless vulnerability is established. It simply does 5 damage without the benefit of exploiting vulnerabilities.

            ### Conclusion:
            Without Vulnerable preceding Card 9 being played, there’s no {SYNERGY_KEYWORD} effect to be noted.

            Final score:
            0
            ---NEXT---
            # Case 10
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - Enemy loses 2 Strength. Exhaust.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Create a copy of an Attack or Power card in your hand.

            ### Order of Events
            - **Playing Card 7 First:**
            - The enemy loses 2 Strength and the card is Exhausted.

            - **Playing Card 10 Next:**
            - Create a copy of an existing Attack or Power.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There is no inherent {SYNERGY_KEYWORD} between these two actions. The effects do not interact, showing no bonuses or unique factors brought into play.

            ### Conclusion:
            No additional interaction comes from playing Card 7 followed by Card 10.

            Final score:
            0
            ---NEXT---
            # Case 11
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - Enemy loses 2 Strength. Exhaust.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            ### Order of Events
            - **Playing Card 7 First:**
            - The enemy loses 2 Strength and is Exhausted.

            - **Playing Card 11 Next:**
            - The next Attack is played twice.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - No direct benefits or amplifications come from the interplay since the lowered strength of the enemy does not impact the damage done by the player.

            ### Conclusion:
            There is not a direct {SYNERGY_KEYWORD} to note.

            Final score:
            0
            ---NEXT---
            # Case 12
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - Enemy loses 2 Strength. Exhaust.

            - **Card 12:**
            - Type: Power
            - Cost: 1
            - Whenever a card is Exhausted, gain 3 Block.

            ### Order of Events
            - **Playing Card 7 First:**
            - The enemy loses 2 Strength followed by card Exhaustion.

            - **Playing Card 12 Next:**
            - Provides Block whenever an Exhausted card occurs.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Upon playing Card 7, it gets Exhasted, but because of the order of play, you do not trigger the gain of 3 Block from Card 12 as a result of card exhaustion in that scenario.

            ### Conclusion:
            This creates a no {SYNERGY_KEYWORD}.

            Final score:
            0
            ---NEXT---
            # Case 13
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 1
            - Deal 8 damage to ALL enemies.

            - **Card 9:**
            - Type: Attack
            - Cost: 1
            - Deal 5 damage. If the enemy is Vulnerable, gain 1 energy and draw 1 card.

            ### Order of Events
            - **Playing Card 8 First:**
            - You deal 8 damage to all enemies.

            - **Playing Card 9 Next:**
            - Card 9 will deal 5 damage, with no effect if enemies have not been made vulnerable yet by Card 8.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - While Card 8 deals AoE damage to all enemies, Card 9's conditional effect to gain an energy and draw a card is not applicable unless an enemy is actually Vulnerable. This sequence fails to provide {SYNERGY_KEYWORD}.

            ### Conclusion:
            In this instance, there is no relevant {SYNERGY_KEYWORD} effect created by this sequence.

            Final score:
            0
            ---NEXT---
            # Case 14
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 1
            - Deal 8 damage to ALL enemies.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Create a copy of an Attack or Power card in your hand.

            ### Order of Events
            - **Playing Card 8 First:**
            - You deal 8 damage to all enemies.

            - **Playing Card 10 Next:**
            - You create a copy of another Attack or Power.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 10 allows you to create a copy of Cards you already have. There’s nothing to improve via the sequence from playing Card 8, unless the copy created fits the criteria of being a beneficial attack.

            ### Conclusion:
            While nothing particularly noteworthy comes from this set order of cards, no enhancements directly connect this {SYNERGY_KEYWORD} either.

            Final score:
            0
            ---NEXT---
            # Case 15
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 1
            - Deal 8 damage to ALL enemies.

            - **Card 11:**
            - Type: Skill
            - Cost: 1
            - This turn, your next Attack is played twice.

            ### Order of Events
            - **Playing Card 8 First:**
            - Deal 8 damage to all enemies.

            - **Playing Card 11 Next:**
            - The next Attack gets played twice.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 8 is played followed by Card 11, where you do not end up repeating the damage output from Card 8.

            ### Conclusion:
            The unfortunate ordering here causes no {SYNERGY_KEYWORD} to arrise.

            Final score:
            0
            ---NEXT---
            # Case 16
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 1
            - Deal 8 damage to ALL enemies.

            - **Card 12:**
            - Type: Power
            - Cost: 1
            - Whenever a card is Exhausted, gain 3 Block.

            ### Order of Events
            - **Playing Card 8 First:**
            - Deal 8 damage to all enemies.

            - **Playing Card 12 Next:**
            - Established block gain condition based on Exhaustion.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There's no interaction between the two cards' respective effects, rendering the sequence lacking any particular advantages.

            ### Conclusion:
            No decisive results or special advantages derive from the interplay here.

            Final score:
            0""")
    },
        # 24, 17, 70, 40; 68, 1, 17, 62; 5
    {
        "X_indices": [24, 17, 70, 40],
        "Y_indices": [68, 1, 17, 62],
        "BundledAnswer": TextUtil.dedent(f"""# Case 1
            ### Card Descriptions:
            - **Card 5:**
            - Type: Attack
            - Cost: 4
            - Costs 1 less energy for each time you lose HP in combat. Deal 18 damage.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 5 First:**
            - You deal 18 damage, potentially with a reduced cost based on previous HP loss.

            - **Playing Card 9 Next:**
            - Assuming you have played no other cards nor have any left (after playing Card 5), you will exhaust no cards, since card 5 was played.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There’s no {SYNERGY_KEYWORD} here since you’re playing Card 5 and then cannot exhaust it with Card 9 for extra damage.

            ### Conclusion:
            The sequence yields no extra damage output distinct from playing each card independently.

            Final score:
            0
            ---NEXT---
            # Case 2
            ### Card Descriptions:
            - **Card 5:**
            - Type: Attack
            - Cost: 4
            - Costs 1 less energy for each time you lose HP in combat. Deal 18 damage.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Gain 5 Block.

            ### Order of Events
            - **Playing Card 5 First:**
            - You deal 18 damage.

            - **Playing Card 10 Next:**
            - You gain 5 Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There is no direct interaction or {SYNERGY_KEYWORD} from playing them in this order. The Block gained doesn’t amplify or minimize the impact of damage dealt by Card 5.

            ### Conclusion:
            No additional advantages or disadvantages come from this sequence.

            Final score:
            0
            ---NEXT---
            # Case 3
            ### Card Descriptions:
            - **Card 5:**
            - Type: Attack
            - Cost: 4
            - Costs 1 less energy for each time you lose HP in combat. Deal 18 damage.

            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            ### Order of Events
            - **Playing Card 5 First:**
            - You deal 18 damage.

            - **Playing Card 6 Next:**
            - You deal 9 damage total (3 damage to a random enemy 3 times).

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage from Card 6 does not enhance or affect the outcome of Card 5. These are two independent attacks without any interplay beyond their individual outputs.

            ### Conclusion:
            There is no effective {SYNERGY_KEYWORD} created in this sequence.

            Final score:
            0
            ---NEXT---
            # Case 4
            ### Card Descriptions:
            - **Card 5:**
            - Type: Attack
            - Cost: 4
            - Costs 1 less energy for each time you lose HP in combat. Deal 18 damage.

            - **Card 11:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            ### Order of Events
            - **Playing Card 5 First:**
            - You deal 18 damage.

            - **Playing Card 11 Next:**
            - This sets up an ongoing effect to draw cards and lose HP.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There’s no substantive interplay here. The damage dealt does not affect Card 11 directly, and since Card 5 is played first, Card 11's effect does not change it.

            ### Conclusion:
            Such sequence offers no beneficial or detrimental {SYNERGY_KEYWORD} effect.

            Final score:
            0
            ---NEXT---
            # Case 5
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 9 damage total (3 damage to a random enemy, 3 times).

            - **Playing Card 9 Next:**
            - You then exhaust all remaining cards and you deal an additional 7 damage for each card exhausted.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - While there’s a reasonable independent benefit from playing both, neither attack card augments the result of the other directly.

            ### Conclusion:
            No significant {SYNERGY_KEYWORD} occurs due to the independent nature of the two cards.

            Final score:
            0
            ---NEXT---
            # Case 6
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Gain 5 Block.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 9 damage total.

            - **Playing Card 10 Next:**
            - You gain 5 Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There’s no synergistic benefit or interaction between these two cards; each offers a separate benefit without affecting the other's outcome.

            ### Conclusion:
            No {SYNERGY_KEYWORD} effect arises in this sequence.

            Final score:
            0
            ---NEXT---
            # Case 7
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            - **Card 6 (again):**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 9 damage total.

            - **Playing Second Card 6 Next:**
            - You now deal another 9 damage (again, 3 damage to random enemies).

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - In this case, each instance of playing Card 6 is stackable, yet remains independent without any alteration to the play interaction from the first play.

            ### Conclusion:
            This demonstrates no {SYNERGY_KEYWORD} effect in terms of damage, since they are the same card without additional amplifying effects, this does just showcase independent outputs.

            Final score:
            0
            ---NEXT---
            # Case 8
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            - **Card 11:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 9 damage total.

            - **Playing Card 11 Next:**
            - The ongoing action begins to lose HP and draw cards at the start of your next turn.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage done does not enhance or influence the effects of Card 11, as the effects remain separate.

            ### Conclusion:
            No distinct {SYNERGY_KEYWORD} occurs from this combination.

            Final score:
            0
            ---NEXT---
            # Case 9
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 2
            - Gain 30 Block. Exhaust.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 7 First:**
            - You gain 30 Block.

            - **Playing Card 9 Next:**
            - You then exhaust all remaining cards and you deal an additional 7 damage for each card exhausted.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The combined play adds no value due to Card 7 not adding to Card 9’s effect, as you gain significant Block and then have exhaustion triggering for damage seperately.

            ### Conclusion:
            The lack {SYNERGY_KEYWORD} here offers a neutral result from this play combination.

            Final score:
            0
            ---NEXT---
            # Case 10
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 2
            - Gain 30 Block. Exhaust.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Gain 5 Block.

            ### Order of Events
            - **Playing Card 7 First:**
            - You gain 30 Block.

            - **Playing Card 10 Next:**
            - You gain another 5 Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There’s no effect seen when playing these two cards in succession. What happens is merely independent Block gain without any added effect related to each card's interactions.

            ### Conclusion:
            No real synergistic benefit emerges from these plays.

            Final score:
            0
            ---NEXT---
            # Case 11
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 2
            - Gain 30 Block. Exhaust.

            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            ### Order of Events
            - **Playing Card 7 First:**
            - You gain 30 Block.

            - **Playing Card 6 Next:**
            - You deal 9 damage total.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The use of Card 7 doesn't interact with or modify the effect of Card 6, as both serve individual purposes with no amplification of effects.

            ### Conclusion:
            No interaction of {SYNERGY_KEYWORD} is present here.

            Final score:
            0
            ---NEXT---
            # Case 12
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 2
            - Gain 30 Block. Exhaust.

            - **Card 11:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            ### Order of Events
            - **Playing Card 7 First:**
            - You gain 30 Block.

            - **Playing Card 11 Next:**
            - You initiate the ongoing effect of losing HP and being able to draw a card.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The effects from the first card don't influence or build upon the second card's ongoing ability. Each acts independently without yielding enhanced effects.

            ### Conclusion:
            There is no {SYNERGY_KEYWORD} effect in this order.

            Final score:
            0
            ---NEXT---
            # Case 13
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Add a random Attack to your hand. It costs 0 this turn. Exhaust.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all cards in your hand. Deal 7 damage for each Exhausted card. Exhaust.

            ### Order of Events
            - **Playing Card 8 First:**
            - You add a random Attack to your hand that costs 0 this turn.

            - **Playing Card 9 Next:**
            - Upon using Card 9, you exhaust the random Attack obtained from Card 8.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 9 exploits the effect of exhausting to gain damage, however since Card 8 does not add to the number of exhaustable cards, they do not interact.

            ### Conclusion:
            This scenario yields no {SYNERGY_KEYWORD} because card 8 does not net extra damage or effects for card 9.

            Final score:
            0
            ---NEXT---
            # Case 14
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Add a random Attack to your hand. It costs 0 this turn. Exhaust.

            - **Card 10:**
            - Type: Skill
            - Cost: 1
            - Gain 5 Block.

            ### Order of Events
            - **Playing Card 8 First:**
            - Gain a random Attack to your hand, at 0 cost.

            - **Playing Card 10 Next:**
            - You gain 5 Block.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 10 creates an additive Block effect independent from whatever Attack was obtained through Card 8. No interaction emerges with significant effects connecting these two cards.

            ### Conclusion:
            No notable {SYNERGY_KEYWORD} is observed from the order of plays.

            Final score:
            0
            ---NEXT---
            # Case 15
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Add a random Attack to your hand. It costs 0 this turn. Exhaust.

            - **Card 6:**
            - Type: Attack
            - Cost: 1
            - Deal 3 damage to a random enemy 3 times.

            ### Order of Events
            - **Playing Card 8 First:**
            - You add a random Attack to your hand costing 0 this turn.

            - **Playing Card 6 Next:**
            - You deal 9 damage total.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There’s no direct {SYNERGY_KEYWORD} generated between these two cards; both actions do their individual roles without affecting the other actions taken.

            ### Conclusion:
            No {SYNERGY_KEYWORD} interaction exists here.

            Final score:
            0
            ---NEXT---
            # Case 16
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Add a random Attack to your hand. It costs 0 this turn. Exhaust.

            - **Card 11:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            ### Order of Events
            - **Playing Card 8 First:**
            - You add a random Attack that costs 0 this turn.

            - **Playing Card 11 Next:**
            - At the next turn, you will lose 1 HP while drawing another card.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - While the benefits acquired from either card don’t intertwine for this sequence,
            their individual effects operate independently, making it a standalone play for each.

            ### Conclusion:
            No {SYNERGY_KEYWORD} is found in this sequence and as such holds no unique {SYNERGY_KEYWORD}.

            Final score:
            0""")
    },
        # 52, 60, 39, 62; 25, 29, 73, 62; 5
    {
        "X_indices": [52, 60, 39, 62],
        "Y_indices": [25, 29, 73, 62],
        "BundledAnswer": TextUtil.dedent(f"""# Case 1
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            - **Card 9:**
            - Type: Skill
            - Cost: 0
            - Lose 3 HP. Gain 2 energy.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 2 energy and then the card is Exhausted.

            - **Playing Card 9 Next:**
            - You lose 3 HP and gain 2 energy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - You essentially regain the energy spent from Card 5 and lose additional health through playing Card 9, but exhausting Card 5 does not directly amplify Card 9's effect.

            ### Conclusion:
            No unique {SYNERGY_KEYWORD} presents itself from this sequence, but you have overall 2 extra energy for the cost of 3 HP.

            Final score:
            0
            ---NEXT---
            # Case 2
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            - **Card 10:**
            - Type: Power
            - Cost: 2
            - Whenever a card is Exhausted, draw 1 card.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 2 energy and then the card is Exhausted.

            - **Playing Card 10 Next:**
            - This card is not played yet, so no cards have been Exhausted when you play it.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There’s no {SYNERGY_KEYWORD} since Card 10 does not trigger any action from the first card being exhausted before it is played.

            ### Conclusion:
            No special advantages generated in this sequence.

            Final score:
            0
            ---NEXT---
            # Case 3
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            - **Card 11:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 2 energy and then the card is Exhausted.

            - **Playing Card 11 Next:**
            - You lose 6 HP, gain 2 energy, and draw 3 cards while exhausting Card 11.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The effect of Card 11 is independent; However, the energy from Card 5 allows for additional card play from Card 10's draws.

            ### Conclusion:
            A {SYNERGY_KEYWORD} effect exists; the played cards just act independently.

            Final score:
            1
            ---NEXT---
            # Case 4
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            - **Card 8:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 2 energy. The card is then Exhausted.

            - **Playing Card 8 Next:**
            - You do not gain any effects at the moment but do set up an ongoing effect.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 8 provides future benefits but not upon its current iteration. Therefore, playing Card 5 generates energy but does not directly influence Card 8's activation.

            ### Conclusion:
            No {SYNERGY_KEYWORD} or notable interaction occurs here.

            Final score:
            0
            ---NEXT---
            # Case 5
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 9:**
            - Type: Skill
            - Cost: 0
            - Lose 3 HP. Gain 2 energy.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 2 Vulnerable and the possibility to gain 1 energy in the next turn.

            - **Playing Card 9 Next:**
            - You lose 3 HP and gain 2 energy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage effect of Vulnerable does not play into the mechanics of Card 9; thus, both cards operate independently here.

            ### Conclusion:
            No {SYNERGY_KEYWORD} effect is observable in this combination.

            Final score:
            0
            ---NEXT---
            # Case 6
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 10:**
            - Type: Power
            - Cost: 2
            - Whenever a card is Exhausted, draw 1 card.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 2 Vulnerable.

            - **Playing Card 10 Next:**
            - This card does not activate yet or draw any cards at this point.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The two cards do not interact at all; thus, they are independent of each other, with no benefit derived from the sequence.

            ### Conclusion:
            No advantageous {SYNERGY_KEYWORD} effect occurs with these two.

            Final score:
            0
            ---NEXT---
            # Case 7
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 11:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 2 Vulnerable.

            - **Playing Card 11 Next:**
            - You could potentially gain 2 energy, draw 3 cards, and exhaust Card 11, but none of these actions will amplify the effect of Card 6.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There’s a small benificial effect between the two cards when combined, since Card 6 lets you play more cards drawn from Card 11.

            ### Conclusion:
            A {SYNERGY_KEYWORD} emerges as more options become available.

            Final score:
            1
            ---NEXT---
            # Case 8
            ### Card Descriptions:
            - **Card 6:**
            - Type: Power
            - Cost: 0
            - Gain 2 Vulnerable. At the start of your turn, gain 1 energy.

            - **Card 8:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 2 Vulnerable.

            - **Playing Card 8 Next:**
            - This establishes your future turns for a draw.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Just like in previous sequences, the gains with each do not present any enhanced interaction; they merely act independently.

            ### Conclusion:
            No bonus or {SYNERGY_KEYWORD} occurs through this sequence as well.

            Final score:
            0
            ---NEXT---
            # Case 9
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - Lose 2 HP. Deal 15 damage.

            - **Card 9:**
            - Type: Skill
            - Cost: 0
            - Lose 3 HP. Gain 2 energy.

            ### Order of Events
            - **Playing Card 7 First:**
            - You lose 2 HP to deal 15 damage.

            - **Playing Card 9 Next:**
            - You lose 3 HP and gain 2 energy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage from Card 7 does not benefit from or amplify the energy gain provided by Card 9; they remain separate experiences.

            ### Conclusion:
            No additional advantages are seen here.

            Final score:
            0
            ---NEXT---
            # Case 10
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - Lose 2 HP. Deal 15 damage.

            - **Card 10:**
            - Type: Power
            - Cost: 2
            - Whenever a card is Exhausted, draw 1 card.

            ### Order of Events
            - **Playing Card 7 First:**
            - You lose 2 HP to deal 15 damage.

            - **Playing Card 10 Next:**
            - Card 10 does not get to influence Card 7 since none is exhausted directly leading to its effects.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There’s no interaction between the two where one enhances the effect of the other; they function separately.

            ### Conclusion:
            No {SYNERGY_KEYWORD} evolves from this play.

            Final score:
            0
            ---NEXT---
            # Case 11
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - Lose 2 HP. Deal 15 damage.

            - **Card 11:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            ### Order of Events
            - **Playing Card 7 First:**
            - You lose 2 HP to deal 15 damage.

            - **Playing Card 11 Next:**
            - You lose 6 HP, gain 2 energy, draw 3 cards, and exhaust the card.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The damage dealt from Card 7 does not alter the lost health interactions provided by Card 11. This remains a standalone interaction.

            ### Conclusion:
            As previously seen, no element of {SYNERGY_KEYWORD} occurs in this case.

            Final score:
            0
            ---NEXT---
            # Case 12
            ### Card Descriptions:
            - **Card 7:**
            - Type: Skill
            - Cost: 1
            - Lose 2 HP. Deal 15 damage.

            - **Card 8:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            ### Order of Events
            - **Playing Card 7 First:**
            - You lose 2 HP to deal 15 damage.

            - **Playing Card 8 Next:**
            - You gain the future ability to lose HP and draw a card but not gain any benefit immediately.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There are no overlaps or enhancements in effect through this interaction.

            ### Conclusion:
            The cards only function on their independent basis.

            Final score:
            0
            ---NEXT---
            # Case 13
            ### Card Descriptions:
            - **Card 8:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            - **Card 9:**
            - Type: Skill
            - Cost: 0
            - Lose 3 HP. Gain 2 energy.

            ### Order of Events
            - **Playing Card 8 First:**
            - You set up the second turn to lose 1 HP and draw a card but gain nothing yet from this iteration.

            - **Playing Card 9 Next:**
            - You lose 3 HP and gain 2 energy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The interaction from the second card does not directly improve or affect the outcome of the first card, however, they open more options for the player.

            ### Conclusion:
            A beneficial {SYNERGY_KEYWORD} effect arises in this sequence.

            Final score:
            1
            ---NEXT---
            # Case 14
            ### Card Descriptions:
            - **Card 8:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            - **Card 10:**
            - Type: Power
            - Cost: 2
            - Whenever a card is Exhausted, draw 1 card.

            ### Order of Events
            - **Playing Card 8 First:**
            - Sets the stage for future turns to lose HP and gain cards.

            - **Playing Card 10 Next:**
            - Does not gain any effects until Exhausted cards come into play.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The {SYNERGY_KEYWORD} is absent, leading to both being independent of the other.

            ### Conclusion:
            No additional benefits occur from this sequence.

            Final score:
            0
            ---NEXT---
            # Case 15
            ### Card Descriptions:
            - **Card 8:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            - **Card 11:**
            - Type: Skill
            - Cost: 0
            - Lose 6 HP. Gain 2 energy. Draw 3 cards. Exhaust.

            ### Order of Events
            - **Playing Card 8 First:**
            - Ongoing effect for future turns is set up by initializing the card.

            - **Playing Card 11 Next:**
            - Immediately allows for the loss of HP in tandem with draw, alongside gaining substantial energy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Because Card 11 gains energy, Card 8's additional draw is benificial.

            ### Conclusion:
            There’s a small {SYNERGY_KEYWORD} between cards in this situation.

            Final score:
            1
            ---NEXT---
            # Case 16
            ### Card Descriptions:
            - **Card 8:**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            - **Card 8 (again):**
            - Type: Power
            - Cost: 0
            - At the start of your turn, lose 1 HP and draw 1 card.

            ### Order of Events
            - **Playing Card 8 First:**
            - You set up effects that will emerge each turn.

            - **Playing Second Card 8 Next:**
            - Similar to the first one, this card also stacks the ongoing functionality without any unique interaction with either.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - No new synergistic effects occur as both actions are redundant. They merely grant similar continuous actions.

            ### Conclusion:
            No advantages or shifts in effects are present in this case.

            Final score:
            0""")
    },
        # 16, 48, 63, 19; 6, 24, 36, 52; 5
    {
        "X_indices": [16, 48, 63, 19],
        "Y_indices": [6, 24, 36, 52],
        "BundledAnswer": TextUtil.dedent(f"""# Case 1
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 8 Block. Draw 1 card.

            - **Card 9:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 8 Block and draw a card.

            - **Playing Card 9 Next:**
            - After drawing a card, you check your hand to see if it only contains Attack cards. If it does, you can deal 14 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There is a potential negative {SYNERGY_KEYWORD} here. By playing Card 5 first, you are drawing a card which will never help fulfill the requirement for playing Card 9, in case you have not drawn another Attack card.
            - However, if the drawn card is an Attack card, Card 9 would gain no additional effect.

            ### Conclusion:
            The effectiveness of Card 9 depends on whether Card 5 allows you to fulfill the condition of having only Attack cards. If it does, you get a total of 14 damage after gaining 8 Block; otherwise, you gain 8 Block and do not attack.

            Final score:
            -1
            ---NEXT---
            # Case 2
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 8 Block. Draw 1 card.

            - **Card 10:**
            - Type: Attack
            - Cost: 4
            - Costs 1 less energy for each time you lose HP in combat. Deal 18 damage.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 8 Block and draw a card.

            - **Playing Card 10 Next:**
            - You then may play Card 10, paying its cost or the reduced cost based on lost HP, and deal 18 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There is a small negative {SYNERGY_KEYWORD} between Cards 5 and 10, as both operate independently, and Card 5 makes Card 10 harder to play.

            ### Conclusion:
            Gaining block here hurts your chances of lossing HP, causing a negative {SYNERGY_KEYWORD}.

            Final score:
            -1
            ---NEXT---
            # Case 3
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 8 Block. Draw 1 card.

            - **Card 11:**
            - Type: Power
            - Cost: 1
            - Whenever you draw a Status or Curse card, deal 6 damage to all enemies.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 8 Block and draw a card.

            - **Playing Card 11 Next:**
            - If the drawn card is a Status or Curse, then Card 11 activates afterward to deal 6 damage to all enemies.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The cards are played in the wrong order to provide a {SYNERGY_KEYWORD}.

            ### Conclusion:
            The combination presents no potential benefit due to the ordering of cards.

            Final score:
            0
            ---NEXT---
            # Case 4
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 1
            - Gain 8 Block. Draw 1 card.

            - **Card 12:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            ### Order of Events
            - **Playing Card 5 First:**
            - You gain 8 Block and draw a card.

            - **Playing Card 12 Next:**
            - You gain 2 energy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The skills operate independent of one another. Card 5 does not influence the energy gain effect in association with Card 12.
            - However, it does provide new options and energy to play those options.

            ### Conclusion:
            A small {SYNERGY_KEYWORD} emerges, and you gain more options overall.

            Final score:
            1
            ---NEXT---
            # Case 5
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 0
            - Deal 10 damage. Shuffle a Dazed into your draw pile.

            - **Card 9:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 10 damage and shuffle a Dazed into your draw pile.

            - **Playing Card 9 Next:**
            - If the conditions are satisfied (no non-Attack cards), you deal 14 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There is a small interconnection between Cards 6 and 9. The drawn Dazed may negatively impact the ability to play Card 9 next.

            ### Conclusion:
            A small negative {SYNERGY_KEYWORD} or arises from this arrangement.

            Final score:
            -1
            ---NEXT---
            # Case 6
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 0
            - Deal 10 damage. Shuffle a Dazed into your draw pile.

            - **Card 10:**
            - Type: Attack
            - Cost: 4
            - Costs 1 less energy for each time you lose HP in combat. Deal 18 damage.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 10 damage and shuffle a Dazed into your draw pile.

            - **Playing Card 10 Next:**
            - You can now pay the card’s cost depending on your HP loss and deal 18 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 10 operates independently of Card 6. Losing HP does not assist in creating further advantages between actions.

            ### Conclusion:
            No enhanced interaction between these two plays.

            Final score:
            0
            ---NEXT---
            # Case 7
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 0
            - Deal 10 damage. Shuffle a Dazed into your draw pile.

            - **Card 11:**
            - Type: Power
            - Cost: 1
            - Whenever you draw a Status or Curse card, deal 6 damage to all enemies.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 10 damage and shuffle Dazed.

            - **Playing Card 11 Next:**
            - The Dazed allows opportunity to enable extra damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The added Daze card makes Card 11's effect more likely to happen.

            ### Conclusion:
            A positive interaction occurs from this combination.

            Final score:
            1
            ---NEXT---
            # Case 8
            ### Card Descriptions:
            - **Card 6:**
            - Type: Attack
            - Cost: 0
            - Deal 10 damage. Shuffle a Dazed into your draw pile.

            - **Card 12:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            ### Order of Events
            - **Playing Card 6 First:**
            - You deal 10 damage and draw a Dazed.

            - **Playing Card 12 Next:**
            - You gain 2 energy with no elevated connection to prior card plays.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Each card continues to operate without aiding additional effectiveness through their execution.
            - However, Card 6 adds the possibility for Card 12 to be drawn in a hand with fewer cards, reducing its effectiveness.

            ### Conclusion:
            A small negative {SYNERGY_KEYWORD} emerges here.

            Final score:
            -1
            ---NEXT---
            # Case 9
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 3
            - Skills cost 0. Whenever you play a Skill, Exhaust it.

            - **Card 9:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 7 First:**
            - Skills now cost 0 energy to play and will be exhausted upon use.

            - **Playing Card 9 Next:**
            - If every card after the use of the Skills is an Attack, it can be played.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Playing Card 7 first allows you to play more skills without cost. This means your ability to play Card 9 becomes higher.

            ### Conclusion:
            Playing a Power card like Card 7 directly supports Card 9 due to the energy cost reduction and exhaustion of Skills, indicates a positive outcome.

            Final score:
            1
            ---NEXT---
            # Case 10
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 3
            - Skills cost 0. Whenever you play a Skill, Exhaust it.

            - **Card 10:**
            - Type: Attack
            - Cost: 4
            - Costs 1 less energy for each time you lose HP in combat. Deal 18 damage.

            ### Order of Events
            - **Playing Card 7 First:**
            - Skills now cost 0 energy to play and will be exhausted upon use.

            - **Playing Card 10 Next:**
            - The effect of playing Card 10 remains unchanged.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The effect of Card 7 does not improve or reduce Card 10's performance, since this Attack depends on HP rather than the Skill effect of Card 7.

            ### Conclusion:
            Therefore, no advantage or disadvantage arises from this interaction creating a neutral setup.

            Final score:
            0
            ---NEXT---
            # Case 11
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 3
            - Skills cost 0. Whenever you play a Skill, Exhaust it.

            - **Card 11:**
            - Type: Power
            - Cost: 1
            - Whenever you draw a Status or Curse card, deal 6 damage to all enemies.

            ### Order of Events
            - **Playing Card 7 First:**
            - Skills now cost 0 and will be exhausted.

            - **Playing Card 11 Next:**
            - Playing this card does not directly interact with the first card as it depends on drawn Status or Curse cards.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Here, no additional benefits or interactions arise between Cards 7 and 11 through this order.

            ### Conclusion:
            Thus, there are no advantages or disadvantages, marking this sequence as neutral.

            Final score:
            0
            ---NEXT---
            # Case 12
            ### Card Descriptions:
            - **Card 7:**
            - Type: Power
            - Cost: 3
            - Skills cost 0. Whenever you play a Skill, Exhaust it.

            - **Card 12:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            ### Order of Events
            - **Playing Card 7 First:**
            - Skills are played at no cost and will be exhausted.

            - **Playing Card 12 Next:**
            - This card would be free to play, providing energy and being exhausted.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Card 12 being played while Card 7 is in effect gives an immediate energy boost—however, the exhausting ability that follows does not create {SYNERGY_KEYWORD} with other cards in hand.

            ### Conclusion:
            The outcome here is advantageous through the energy gain but doesn't create further interactions with respect to both cards specific to the {SYNERGY_KEYWORD} order, thus making it a moderate advantage.

            Final score:
            1
            ---NEXT---
            # Case 13
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Gain 7 Block. Exhaust a random card from your hand.

            - **Card 9:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 8 First:**
            - You gain 7 Block but exhaust a random card from your hand, potentially losing a non-Attack card.

            - **Playing Card 9 Next:**
            - This depends on whether you still have Attack cards remaining in hand. If you have lost a non-Attack as a consequence of Card 8, then you can play Card 9 easier.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The probability of exhausting a non-Attack card allows for playing Card 9.

            ### Conclusion:
            As such, this sequence has the potential for a positive {SYNERGY_KEYWORD} because Card 8 helps to play Card 9.

            Final score:
            1
            ---NEXT---
            # Case 14
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Gain 7 Block. Exhaust a random card from your hand.

            - **Card 10:**
            - Type: Attack
            - Cost: 4
            - Costs 1 less energy for each time you lose HP in combat. Deal 18 damage.

            ### Order of Events
            - **Playing Card 8 First:**
            - You gain 7 Block and exhaust a random card.

            - **Playing Card 10 Next:**
            - The effectiveness of Card 10 is determined independently from Card 8’s set-up regarding damage or cost reduction.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Given no influence on Card 10, this sequence registers as a neutral {SYNERGY_KEYWORD} as no interplay exists between the two.

            ### Conclusion:
            Thus, the result is absent of any unique interactions creating a neutral outcome.

            Final score:
            0
            ---NEXT---
            # Case 15
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Gain 7 Block. Exhaust a random card from your hand.

            - **Card 11:**
            - Type: Power
            - Cost: 1
            - Whenever you draw a Status or Curse card, deal 6 damage to all enemies.

            ### Order of Events
            - **Playing Card 8 First:**
            - You gain 7 Block and exhaust a random card.

            - **Playing Card 11 Next:**
            - Card 11 effects depend entirely on whether you draw a Status or Curse.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Given no influence on Card 11, this sequence registers as a neutral {SYNERGY_KEYWORD} as no interplay exists between the two.

            ### Conclusion:
            Thus, the result is absent of any unique interactions creating a neutral outcome.

            Final score:
            0
            ---NEXT---
            # Case 16
            ### Card Descriptions:
            - **Card 8:**
            - Type: Skill
            - Cost: 1
            - Gain 7 Block. Exhaust a random card from your hand.

            - **Card 12:**
            - Type: Skill
            - Cost: 1
            - Gain 2 energy. Exhaust.

            ### Order of Events
            - **Playing Card 8 First:**
            - You gain 7 Block and exhaust a random card.

            - **Playing Card 12 Next:**
            - After exhausting another card, you can gain energy.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The interaction is entirely independent; however, losing your options for Card 12's energy increases the possibility of leftover energy, which does not carry over between turns.

            ### Conclusion:
            This sequence of plays results in a small negative {SYNERGY_KEYWORD}.

            Final score:
            -1""")
    },
        # 23, 16, 69, 15; 54, 6, 21, 23; 5
    {
        "X_indices": [23, 16, 69, 15],
        "Y_indices": [54, 6, 21, 23],
        "BundledAnswer": TextUtil.dedent(f"""# Case 1
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 0
            - Draw 3 cards. You cannot draw additional cards this turn.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all non-Attack cards in your hand. Deal 16 damage.

            ### Order of Events
            - **Playing Card 5 First:**
            - You draw 3 cards, expanding your hand.

            - **Playing Card 9 Next:**
            - When Card 9 is played, you exhaust all non-Attack cards including those drawn from Card 5, assuming some of them were not Attack cards. Regardless, you will deal 16 damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Depending on the draw from Card 5, if non-Attack cards were drawn, those cards would be exhausted, but there isn't any beneficial interaction or {SYNERGY_KEYWORD} between the two as no additional value is derived specifically from the order or impacts of Card 5 before Card 9.

            ### Conclusion:
            This sequence does not yield any notable advantages, meaning the disadvantages shine through. It is classified as having negative {SYNERGY_KEYWORD} effect.

            Final score:
            -1
            ---NEXT---
            # Case 2
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 0
            - Draw 3 cards. You cannot draw additional cards this turn.

            - **Card 10:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 5 First:**
            - You draw 3 cards.

            - **Playing Card 10 Next:**
            - Card 10 requires that every card in your hand is an Attack type, which is impossible to fulfill after playing Card 5 unless all cards drawn were Attack cards.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - There is no benefit or validity to play Card 10 after Card 5 since the situation restricts Card 10 entirely by removing the potential of playing it.

            ### Conclusion:
            Given that Card 10 can't be played after drawing from Card 5, this exhibits negative {SYNERGY_KEYWORD} effects.

            Final score:
            -1
            ---NEXT---
            # Case 3
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 0
            - Draw 3 cards. You cannot draw additional cards this turn.

            - **Card 11:**
            - Type: Skill
            - Cost: 0
            - Draw 1 card. Place a card from your hand on top of your draw pile. Exhaust.

            ### Order of Events
            - **Playing Card 5 First:**
            - You draw 3 cards.

            - **Playing Card 11 Next:**
            - You draw no additional card because of Card 5. Then, you place a card from your hand back on top of your draw pile.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The initial card draw from Card 5 is effective, followed by Card 11, which does not get to draw because of Card 5.

            ### Conclusion:
            Because the effects cut off Card 11's draw, the sequence leads to a negative {SYNERGY_KEYWORD}.

            Final score:
            -1
            ---NEXT---
            # Case 4
            ### Card Descriptions:
            - **Card 5:**
            - Type: Skill
            - Cost: 0
            - Draw 3 cards. You cannot draw additional cards this turn.

            ### Order of Events
            - **Playing Card 5 First:**
            - You draw 3 cards.

            - **Playing Card 5 Again:**
            - Card 5 states you cannot draw additional cards this turn, leading to no new draws.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Playing Card 5 first followed again by the same card produces no further advantage and just wastes energy. The limit on drawing more cards leads to ineffective redundancy.

            ### Conclusion:
            The combination of plays leads to a reduction in effectiveness, a negative {SYNERGY_KEYWORD}.

            Final score:
            -1
            ---NEXT---
            # Case 5
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - Gain 8 Block. Draw 1 card.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all non-Attack cards in your hand. Deal 16 damage.

            ### Order of Events
            - **Playing Card 6 First:**
            - Gain 8 Block and draw 1 card.

            - **Playing Card 9 Next:**
            - You now exhaust the remaining non-Attack cards in your hand, which could include the card drawn from Card 6.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Playing Card 6 first gives a card draw, and the card drawn can be a non-Attack card. This would then be removed by Card 9.

            ### Conclusion:
            The Exhaustion leads to a direct negative {SYNERGY_KEYWORD}.

            Final score:
            -1
            ---NEXT---
            # Case 6
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - Gain 8 Block. Draw 1 card.

            - **Card 10:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 8 Block and draw 1 card.

            - **Playing Card 10 Next:**
            - This card will only work worth if all cards in hand are Attack types; that means unless the card drawn through Card 6 was one, there’s no possibility of utilizing this effectively.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The outcome of Block gained does not project into a beneficial play with Card 10 unless favorable circumstances arise. So the only thing that happens is the drawn cards possibly locking possible damage output.

            ### Conclusion:
            The play sequence fails to yield a cooperative interaction, hence keeping things disjointed.

            Final score:
            -1
            ---NEXT---
            # Case 7
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - Gain 8 Block. Draw 1 card.

            - **Card 11:**
            - Type: Skill
            - Cost: 0
            - Draw 1 card. Place a card from your hand on top of your draw pile. Exhaust.

            ### Order of Events
            - **Playing Card 6 First:**
            - You gain 8 Block and draw a card.

            - **Playing Card 11 Next:**
            - Follow up this action for additional drawing and returning a card to the top of your draw pile.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The opportunity to rotate or maintain dynamic control is effective here, with drawing leading to the ability to recast priority cards. This works well through both skills having an interaction that enriches ongoing plays.

            ### Conclusion:
            Thus, the sequence generates a positive interplay.

            Final score:
            1
            ---NEXT---
            # Case 8
            ### Card Descriptions:
            - **Card 6:**
            - Type: Skill
            - Cost: 1
            - Gain 8 Block. Draw 1 card.

            - **Card 5:**
            - Type: Skill
            - Cost: 0
            - Draw 3 cards. You cannot draw additional cards this turn.

            ### Order of Events
            - **Playing Card 6 First:**
            - Gain 8 Block and draw 1 card.

            - **Playing Card 5 Next:**
            - Draw 3 additional cards.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Here, the plays yield a large amount of draw, leading to a sprawling hand but dont enhance each others effects.

            ### Conclusion:
            The cards give more draw, but do not enhance each other's effects

            Final score:
            0
            ---NEXT---
            # Case 9
            ### Card Descriptions:
            - **Card 7:**
            - Type: Attack
            - Cost: 2
            - Deal 21 damage to ALL enemies. Add a Burn into your discard pile.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all non-Attack cards in your hand. Deal 16 damage.

            ### Order of Events
            - **Playing Card 7 First:**
            - You deal 21 damage and add a Burn to the discard pile.

            - **Playing Card 9 Next:**
            - Subsequently, you exhaust all non-Attack cards and deal additional damage.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The Burn added by Card 7 can affect player strategy but the attacks remain independent of each other.

            ### Conclusion:
            While you may be able to exhaust the burn card, it is not significant enough to matter. There is no {SYNERGY_KEYWORD}.

            Final score:
            0
            ---NEXT---
            # Case 10
            ### Card Descriptions:
            - **Card 7:**
            - Type: Attack
            - Cost: 2
            - Deal 21 damage to ALL enemies. Add a Burn into your discard pile.

            - **Card 10:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 7 First:**
            - Deal 21 damage and incur a Burn from which counts but a correlation shines true in that it does not conditionally affect the play afterwards.

            - **Playing Card 10 Next:**
            - The likelihood of ability to play card 10 post remains dependent on current card draw. Otherwise, it works outside of a continuous effect.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The ability to now draw the Burn card and lose your ability to play Card 10 makes this interference realistic to expect.

            ### Conclusion:
            The play outcome fails to bring out positive effects, and leaves behind only negative {SYNERGY_KEYWORD}.

            Final score:
            -1
            ---NEXT---
            # Case 11
            ### Card Descriptions:
            - **Card 7:**
            - Type: Attack
            - Cost: 2
            - Deal 21 damage to ALL enemies. Add a Burn into your discard pile.

            - **Card 11:**
            - Type: Skill
            - Cost: 0
            - Draw 1 card. Place a card from your hand on top of your draw pile. Exhaust.

            ### Order of Events
            - **Playing Card 7 First:**
            - The play’s intent manifests damage with Burn provided afterwards.

            - **Playing Card 11 Next:**
            - You can execute drawing followed with establishing card priority in retreat which follows interaction.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Each card’s effects here play independently. The initial attack allows damage but follows up seamlessly when contrast recall comes into play from any drawn behavior post alignment assessment.

            ### Conclusion:
            Despite of outcomes which can deter health overall, no combos or interactions between resultant independence fall out too.

            Final score:
            0
            ---NEXT---
            # Case 12
            ### Card Descriptions:
            - **Card 7:**
            - Type: Attack
            - Cost: 2
            - Deal 21 damage to ALL enemies. Add a Burn into your discard pile.

            - **Card 5:**
            - Type: Skill
            - Cost: 0
            - Draw 3 cards. You cannot draw additional cards this turn.

            ### Order of Events
            - **Playing Card 7 First:**
            - You apply damage alongside a Burn.

            - **Playing Card 5 Next:**
            - That is to say, following up allows behavior dependent drawing.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Following up with the draw makes the Burn card more likely to be drawn this turn.

            ### Conclusion:
            This higher chance of getting the Burn card leads to a negative {SYNERGY_KEYWORD} between card pair.

            Final score:
            -1
            ---NEXT---
            # Case 13
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Draw 1 card.

            - **Card 9:**
            - Type: Attack
            - Cost: 2
            - Exhaust all non-Attack cards in your hand. Deal 16 damage.

            ### Order of Events
            - **Playing Card 8 First:**
            - 9 damage and follow up with draw.

            - **Playing Card 9 Next:**
            - Then proceed to deal an additional 16.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The draw directly increases your odds of Exhausting more cards from Card 9.

            ### Conclusion:
            This interference leads to a negative {SYNERGY_KEYWORD}.

            Final score:
            -1
            ---NEXT---
            # Case 14
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Draw 1 card.

            - **Card 10:**
            - Type: Attack
            - Cost: 0
            - Can only be played if every card in your hand is an Attack. Deal 14 damage.

            ### Order of Events
            - **Playing Card 8 First:**
            - Deal damage again while ensuring simultaneous drawing available.

            - **Playing Card 10 Next:**
            - Again this requires that all current cards be Attack cards to play effectively.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - The draw directly decreases your odds of being able to play Card 10.

            ### Conclusion:
            The detrimental effects of drawing before Card 10 makes the sequence harder to achieve.

            Final score:
            -1
            ---NEXT---
            # Case 15
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Draw 1 card.

            - **Card 11:**
            - Type: Skill
            - Cost: 0
            - Draw 1 card. Place a card from your hand on top of your draw pile. Exhaust.

            ### Order of Events
            - **Playing Card 8 First:**
            - Playing onto damage occurs followed up by a card draw.

            - **Playing Card 11 Next:**
            - Evaluate options which come from any replacements seen after card draw is executed.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Because you are able to choose from more cards to add to the top, Card 8 benifits Card 11's effect.

            ### Conclusion:
            These two cards lead to a benificial {SYNERGY_KEYWORD} as you gain more options for play.

            Final score:
            1
            ---NEXT---
            # Case 16
            ### Card Descriptions:
            - **Card 8:**
            - Type: Attack
            - Cost: 1
            - Deal 9 damage. Draw 1 card.

            - **Card 5:**
            - Type: Skill
            - Cost: 0
            - Draw 3 cards. You cannot draw additional cards this turn.

            ### Order of Events
            - **Playing Card 8 First:**
            - Initiate damage then assign card draw.

            - **Playing Card 5 Next:**
            - Follow up drawing additional cards, leading to increased chances of future availability.

            ### Analyzing the {SYNERGY_KEYWORD_CAPITALIZED}:
            - Although you can draw more cards,there is a major absence in joint effects or benefits.

            ### Conclusion:
            The interplay yields no complimentary or negative benefits from your action chain.

            Final score:
            0""")
    },
]

def dump_json(example_chat, outfile):

    json_requset = example_chat.as_fine_tuning_example()
    json.dump(json_requset, outfile)
    outfile.write('\n')

class Counter:
    def __init__(self, min_count:int, max_count:int|None):
        assert max_count is None or max_count >= min_count
        assert max_count is None or max_count >= 0
        self.min_count = min_count
        self.max_count = max_count
        self.counter = 0

    def count(self):
        self.counter += 1
    
    def min_reached(self):
        return self.counter >= self.min_count
    
    def max_reached(self):
        return self.max_count is not None and self.counter >= self.max_count

if __name__ == "__main__":
    from llm_connector import OpenAIChat
    from sts_prompts import get_sts_prompts, get_single_card_ask,\
        get_multi_card_bundle_ask, AskType
    import pandas as pd
    import json
    import time
    ask_type = AskType.Negative_or_Positive_Revised
    system_prompt, prompts, responses, next_card_number = get_sts_prompts(ask_type=ask_type)
    chat = OpenAIChat(OpenAIChat.OpenAIModel.GPT_4O_mini, chat_format=False, system_message=system_prompt)
    for prompt, response in zip(prompts, responses):
        chat.inject(prompt, response)
    df = pd.read_csv("IronClad Card Names.csv")
    output_filename = f"finetune_dataset{int(time.time())}"
    with open(f'{output_filename}.jsonl', 'w') as outfile:
        counter = Counter(10, None)
        while not counter.min_reached():
            for example in examples:
                x_indices = example["X_indices"]
                y_indices = example["Y_indices"]
                x_cards = [df.iloc[ind] for ind in x_indices]
                y_cards = [df.iloc[ind] for ind in y_indices]
                df = pd.read_csv("IronClad Card Names.csv")
                if ask_type == AskType.NP_Bundle_Revised:
                    example_chat = chat.copy()
                    prompt, ids, _ = get_multi_card_bundle_ask(x_cards, y_cards, x_indices, y_indices, next_card_number)
                    example_chat.inject(prompt, example["BundledAnswer"])
                    dump_json(example_chat, outfile)
                    counter.count()
                elif ask_type == AskType.Negative_or_Positive_Revised:
                    prompts = []
                    _, _, bundle_id_mapping = get_multi_card_bundle_ask(x_cards, y_cards, x_indices, y_indices, next_card_number)
                    # TODO find a better way to do this.
                    # This is dangerous because it assumes the order of questions are always X*Y
                    # removes the case number and splits the cases
                    answers = ['\n'.join(answer.split('\n')[1:]) for answer in example["BundledAnswer"].split("---NEXT---\n")]
                    for x, (x_card, x_ind) in enumerate(zip(x_cards, x_indices)):
                        for y, (y_card, y_ind) in enumerate(zip(y_cards, y_indices)):
                            prompt, ids, single_id_mapping = get_single_card_ask(x_card, y_card, x_ind, y_ind, next_card_number)
                            for original_id, single_text_id in single_id_mapping.items():
                                bundle_text_id = bundle_id_mapping[original_id]
                                answers[len(prompts)] = answers[len(prompts)].\
                                    replace(f"Card {bundle_text_id}", f"Card {single_text_id}")
                            prompts.append(prompt)
                    for prompt, answer in zip(prompts, answers):
                        example_chat = chat.copy()
                        assert 'Case' not in answer
                        example_chat.inject(prompt, answer)
                        dump_json(example_chat, outfile)
                        counter.count()
                        if counter.max_reached():
                            break
                else:
                    raise Exception("Unknown ask type for creating fine-tuning examples")
                if counter.max_reached():
                    break
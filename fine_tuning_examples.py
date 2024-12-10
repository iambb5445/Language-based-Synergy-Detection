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
                    prompt, ids = get_multi_card_bundle_ask(x_cards, y_cards, x_indices, y_indices, next_card_number)
                    example_chat.inject(prompt, example["BundledAnswer"])
                    dump_json(example_chat, outfile)
                    counter.count()
                elif ask_type == AskType.Negative_or_Positive_Revised:
                    prompts = []
                    # TODO find a better way to do this.
                    # This is dangerous because it assumes the order of questions are always X*Y
                    for x_card, x_ind in zip(x_cards, x_indices):
                        for y_card, y_ind in zip(y_cards, y_indices):
                            prompt, ids = get_single_card_ask(x_card, y_card, x_ind, y_ind, next_card_number)
                            prompts.append(prompt)
                    # removes the case number and splits the cases
                    answers = ['\n'.join(answer.split('\n')[1:]) for answer in example["BundledAnswer"].split("---NEXT---\n")]
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
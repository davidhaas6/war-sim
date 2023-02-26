from deck import CardDeck
import tqdm
import pandas as pd


def game_over():
    if len(deck1) > len(deck2):
        print("* PLAYER 1 WINS")
    elif len(deck1) < len(deck2):
        print("* PLAYER 2 WINS")

    else:
        print("* TIE ????")
    # print(f"\n\ngame over\nDeck1 - {deck1}\n\nDeck2 - {deck2}")


def card_tie(cards_in_pot: list):
    # print(f"\tLengths going into tie: {len(deck1)}, {len(deck2)} ")
    cards1 = deck1.playCards(4)
    cards2 = deck2.playCards(4)

    cards_to_win = cards1 + cards2 + cards_in_pot

    if not cards1 or not cards2:  # someone ran out
        if cards1: deck1.addCards(cards_to_win)
        elif cards2: deck2.addCards(cards_to_win)
        return 

    if cards1[-1] > cards2[-1]:
        # print(f"\tPlayer 1 won tie: {cards1} vs {cards2}")
        deck1.addCards(cards_to_win)
        return 1
    elif cards1[-1] < cards2[-1]:
        # print(f"\tPlayer 2 won tie: {cards1} vs {cards2}")
        deck2.addCards(cards_to_win)
        return 2
    else:
        # print(f"\tPlayers tied again: {cards1} vs {cards2}")
        return card_tie(cards_to_win)

results = []
for k in tqdm.trange(10000):
    deck1 = CardDeck(numCards=26)
    deck2 = deck1.complementDeck()
    
    for i in range(1000):
        # print(i)
        card1 = deck1.playCards(1)
        card2 = deck2.playCards(1)

        if not card1 or not card2:
            if card1: deck1.addCards(card1)
            elif card2: deck2.addCards(card2)
            # game_over()
            results.append({'turn': i, 'winner': 1 if card1 else 2})
            # print(results)
            break
        else:
            card1 = card1[0]
            card2 = card2[0]
            if type(card1) != int or type(card2) != int:
                print("********** BAD CARD TYPE ******")

        if card1 > card2:
            # print(f"{i}: Player 1 won hand: {card1} vs {card2}")
            deck1.addCards([card1, card2])
        elif card1 < card2:
            # print(f"{i}: Player 2 won hand: {card1} vs {card2}")
            deck2.addCards([card1, card2])
        else:
            # print(f"{i}: Tie: {card1} vs {card2}")
            # print("Lengths: {len(deck1)}, {len(deck2)} ")
            result = card_tie([card1, card2])
            if not result:
                winner = 1 if len(deck1) > len(deck2) else 2 
                # game_over()
                results += [{'turn': i, 'winner': winner}]
                break

        if len(deck1) + len(deck2) != 52:
            print(f"{i} (post): Lengths: {len(deck1)}, {len(deck2)} ")
            print("BAD CARD LENGTHS")
            break
    
# print(f"{results}")
df = pd.DataFrame(results)
print(df)
print(df.describe())
ax = df.turn.plot.hist(title="Number of turns to win War", bins=50)
ax.figure.savefig('trials.pdf')
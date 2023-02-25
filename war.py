from deck import CardDeck

deck1 = CardDeck(numCards=26)
deck2 = deck1.complementDeck()

def game_over():
    print(f"\n\ngame over\nDeck1 - {deck1}\n\nDeck2 - {deck2}")


def card_tie():
    print(f'Lengths going into tie: {len(deck1)}, {len(deck2)} ')
    cards1 = deck1.playCards(4)
    cards2 = deck2.playCards(4)

    if not cards1 or not cards2:  # someone ran out
        return False
    
    if cards1[3] > cards2[3]: 
        print(f"Player 1 won tie: {cards1} vs {cards2}")
        deck1.addCards(cards1+cards2)
    elif cards1[3] < cards2[3]: 
        print(f"Player 2 won tie: {cards1} vs {cards2}")
        deck2.addCards(cards1+cards2)
    else: 
        print(f"Players tied again: {cards1} vs {cards2}")
        return card_tie()

    return True

for i in range(100):       
    print(f'{i}: Lengths: {len(deck1)}, {len(deck2)} ') 
    card1 = deck1.playCards(1)
    card2 = deck2.playCards(1)

    if not card1 or not card2:
        game_over()
        break
    else:
        card1=card1[0]
        card2=card2[0]

    if card1 > card2:
        print(f"Player 1 won hand: {card1} vs {card2}")
        deck1.addCards([card1,card2])
    elif card1 < card2:
        print(f"Player 2 won hand: {card1} vs {card2}")
        deck2.addCards([card1,card2])
    else:
        result = card_tie()
        print(f"Tie: {card1} vs {card2}")
        # if not result:
        #     game_over()
        #     break
        
        

game_over()
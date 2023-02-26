import random


class CardDeck:
    def __init__(self, cards=None, numCards=None) -> None:
        self.discard_pile = []
        if cards != None:
            if type(cards) != list:
                raise ValueError("cards must be a list")
            self.deck = cards

        elif numCards != None:
            if numCards > 52 or numCards < 0:
                raise ValueError("numCards must be between 0 and 52")
            self.deck = CardDeck.fullDeck()[: int(numCards)]

        else:
            raise ValueError("Either cards or numCards must be specified")


    def playOne(self):
        return self.playCards(1)

    
    def playCards(self,k:int) -> list:
        if len(self.deck) + len(self.discard_pile) < k:
                return []
        elif len(self.deck) < k:
            self.refreshDeck()

        return [self.deck.pop(0) for _ in range(k)]
    

    def addCards(self,cards: list) -> None:
        self.discard_pile += cards


    def refreshDeck(self) -> None:
        """ Shuffles the discard pile and adds at the end of the deck """
        random.shuffle(self.discard_pile)
        self.deck += self.discard_pile
        self.discard_pile = []

    
    def complementDeck(self):
        complement = CardDeck.fullDeck()
        for card in self.deck:
            complement.remove(card)
        return CardDeck(cards=list(complement))


    @staticmethod
    def fullDeck(shuffle=True):
        # J = 11, Q = 12, K = 13, A = 14
        deck = [card for _ in range(4) for card in range(2, 15)]
        if shuffle:
            deck = random.sample(deck, len(deck))
        return deck

    def __str__(self) -> str:
        return f'{len(self.deck) + len(self.discard_pile)} cards:\n{self.deck}\ndiscard: {self.discard_pile}'
    
    def __len__(self) -> int:
        return len(self.deck) + len(self.discard_pile)


CardDeck.fullDeck()

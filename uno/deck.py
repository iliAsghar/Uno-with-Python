from uno.card import Card

class Deck:
    def __init__(self, count):
        self.cards = []
        for i in range(1, count + 1):
            card = Card("Red", i)
            self.cards.append(card)
        for i in range(1, count + 1):
            card = Card("Blue", i)
            self.cards.append(card)
        for i in range(1, count + 1):
            card = Card("Yellow", i)
            self.cards.append(card)
        for i in range(1, count + 1):
            card = Card("Green", i)
            self.cards.append(card)
    def show_cards(self):
        for c in self.cards:
            print(c.__str__())

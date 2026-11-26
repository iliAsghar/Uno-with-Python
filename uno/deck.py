from uno.card import Card

class Deck:
    def __init__(self, count):
        self.cards = []
        for i in range(1, count + 1):
            card = Card("red", i)
            self.cards.append(card)
    def show_cards(self):
        for c in self.cards:
            print(c.__str__())

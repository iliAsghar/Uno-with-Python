class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"Card: {self.color} {self.value}"

# test
# c1 = Card("red", 8)
# print(c1.__str__())
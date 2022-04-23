from random import shuffle
from card import Card


class Deck:
    def __init__(self) -> None:
        self.cards = []
        for color in Card.possible_colors:
            for value in Card.possible_values:
                self.cards.append(
                    Card(color=color, value=value)
                )

    def shuffle(self):
        shuffle(self.cards)

    def hit(self):
        return self.cards.pop()
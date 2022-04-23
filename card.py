"""BlackJack Python game"""


class InvalidColor(Exception):
    """Exception when color is invalid"""


class InvalidValue(Exception):
    """Exception when value is invalid"""


class Card:
    """Card abstraction"""
    possible_colors = {
        'spades': '♤',
        'diamonds': '♢',
        'hearts': '♡',
        'clubs': '♧'
    }
    possible_values = list(range(2, 11)) + [
        'Ace',
        'Jack',
        'Queen',
        'King'
    ]

    def __init__(self, color, value) -> None:
        if color not in self.possible_colors:
            raise InvalidColor('Invalid card color')
        self.color = self.possible_colors[color]
        if value not in self.possible_values:
            raise InvalidValue('Invalid card value')
        self.value = value

    def __repr__(self) -> str:
        return f'{self.value} -> {self.color}'

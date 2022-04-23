"""Card tests"""
import pytest
from card import Card, InvalidColor, InvalidValue


def test_creation():
    card = Card('hearts', 'Ace')
    assert card.color == '\u2661'
    assert card.value == 'Ace'


def test_creation_wrong_value():
    with pytest.raises(InvalidValue) as message:
        card = Card('hearts', 'A')
        assert message == 'Invalid card value'


def test_creation_wrong_color():
    with pytest.raises(InvalidColor) as message:
        card = Card('xxx', 'Ace')
        assert message == 'Invalid card value'


def test_card_representation():
    assert repr(Card('spades', 'Ace')) == 'Ace -> ♤'
    assert repr(Card('diamonds', 'Ace')) == 'Ace -> ♢'
    assert repr(Card('hearts', 'Ace')) == 'Ace -> ♡'
    assert repr(Card('clubs', 'Ace')) == 'Ace -> ♧'

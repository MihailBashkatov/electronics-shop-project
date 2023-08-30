"""Здесь надо написать тесты с использованием pytest для модуля item."""
import os

import pytest

from src.InstantiateCSVError import InstantiateCSVError
from src.item import Item


def test_calculate_total_price():
    item = Item('toy', 10.5, 3)
    assert item.calculate_total_price() == 31.5
    assert type(item.calculate_total_price()) == float


def test_apply_discount():
    item = Item('toy', 10, 3)
    Item.pay_rate = 0.7
    assert item.apply_discount() == 7
    assert type(item.calculate_total_price()) == float


def test_name():
    item = Item('toy', 10, 3)
    item.name = 'water'
    assert item.name == 'water'
    item.name = 'crocodile_green'
    assert item.name == 'crocodile_'


def test_string_to_number():
    item = Item('toy', 10, 3)
    assert item.string_to_number('10') == 10
    assert item.string_to_number('1.3') == 1
    assert item.string_to_number('9.8') == 9

def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    for item in Item.all:
        assert repr(item)[0:4] == "Item"
        assert repr(item)[-1] == ")"
        for letter in str(item.name):
            assert letter.isalpha()

    Item.instantiate_from_csv(os.path.join('..', 'src', 'no_file.csv'))
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv(os.path.exists(os.path.join('..', 'src', 'it.csv')))



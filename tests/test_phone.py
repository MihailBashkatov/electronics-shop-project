import pytest
from src.phone import Phone
from src.item import Item

phone_1 = Phone('Samsung', 20_000, 10, 4)
item_1 = Item('Nokia', 10_000, 20)
item_2 = Item('Nokia', 10_000, 40)


def test_phone_number_of_sim():
    """ Проверка на соответствие number_of_sim классу int"""
    assert isinstance(phone_1.number_of_sim, int)
    assert phone_1.number_of_sim == 4


def test_add_insance():
    """ Проверка на возможность складывать экземпляры Item и Phone. Другие классы выдают ошибку"""
    assert item_1 + phone_1 == 30
    assert phone_1 + item_2 == 50
    assert 10 + phone_1 == 'Первое слагаемое не является атрибутом класса Item'


def test_number_of_sim():
    """ Проверка на количество number_of_sim больше 0"""
    with pytest.raises(ValueError):
        phone_1.number_of_sim = 0
        phone_2 = Phone('Samsung', 20_000, 10, 0)
        assert phone_1, phone_2

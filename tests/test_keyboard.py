import pytest

from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)

def test_str_method():
    """ Assert if name is correct"""
    assert str(kb) == "Dark Project KD87A"

def test_language():
    """ Asserting if initially language is EN """
    assert kb.language == 'EN'

def test_change_language():
    """ Asserting if language is changing into RU"""
    kb.change_lang()
    assert kb.language == 'RU'

def test_several_changes():
    """ Asserting if language changing into RU in case of double change"""
    kb.change_lang()
    assert kb.language == 'EN'
    kb.change_lang().change_lang()
    assert kb.language == 'EN'

def test_manual_change_language():
    """ Assering if no possibility to insert language manually"""
    with pytest.raises(AttributeError):
        kb.language = 'CN'

#
# assert str(kb.language) == "EN"
# #
# kb.change_lang()
# assert str(kb.language) == "RU"
# #
# # # Сделали RU -> EN -> RU
# kb.change_lang().change_lang()
# assert str(kb.language) == "RU"
#
# kb.language = 'CH'
# # # AttributeError: property 'language' of 'Keyboard' object has no setter
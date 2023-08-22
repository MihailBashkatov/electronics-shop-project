from src.item import Item


class Mixin:
    """ Class for languages, where they are stored and can be changed"""

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.__language = 'EN'

    def change_lang(self):
        # if
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        return self

    @property
    def language(self):
        return self.__language


class Keyboard(Mixin, Item):
    """ Class, which is initializing a Keyboard"""

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

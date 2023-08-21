from src.item import Item


class Phone(Item):
    """
    Класс для представления телефона. Наследуется от Items
    """

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """ Метод позволяет складывать только экземпляры класса Phone and Item,
        где первое слагаемое - экземпляр класса Phone"""
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            return 'Второе слагаемое не является атрибутом класса Item'

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if not isinstance(number_of_sim, int) or number_of_sim < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__number_of_sim = number_of_sim

from src.item import Item


class Phone(Item):
    """
    Класс для представления телефона. Наследуется от Items
    """

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)

        # Если количество сим-карт меньше одной, то вызывается ошибка и выводится сообщение пользователю
        if number_of_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):

        # Если количество сим-карт меньше одной, то вызывается ошибка и выводится сообщение пользователю
        if value < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        self.__number_of_sim = value

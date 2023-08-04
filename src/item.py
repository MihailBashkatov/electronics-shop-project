import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price *= self.pay_rate
        return self.price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) > 10:
            self.__name = value[0:10]
        else:
            self.__name = value

    @staticmethod
    def string_to_number(string):
        if '.' in string:
            return int(float(string))
        else:
            return int(string)

    @classmethod
    def instantiate_from_csv(cls):
        with open('../src/items.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                for value in row.values():
                    value_decoded = value.encode('ISO-8859-1').decode('cp1251')
                    value_new = value_decoded.split()
                    cls.all.append(cls(value_new[0], value_new[1], value_new[2]))

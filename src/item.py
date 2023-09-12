import csv
import pathlib


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
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

        Item.all.append(self)


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        """
        Приватит атрибут name
        """
        return self.__name


    @name.setter
    def name(self, name_string: str):
        """
        Проверяет длину имени и если больше 10, то сокращает до первых 10 символов
        """
        if len(name_string) > 10:
            self.__name = name_string[:10]
        else:
            self.__name = name_string

    @classmethod
    def instantiate_from_csv(cls):
        """
        Берет перечень объектов из файла CSV и делает из них экземпляры класс Item
        """
        cls.all = []
        with (open('../src/items.csv', "r", encoding='Windows-1251') as csvfile):
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(text: str) -> int:
        """
        Проверят входящее значение на число, превращает строку в целое число
        """
        if text.isdigit():
            return int(text)
        else:
            x = float(text)
            return int(x)

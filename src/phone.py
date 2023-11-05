from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim


    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    def __add__(self, other):
        return self.quantity + other.quantity if isinstance(other, Phone) else print("Эти объекты нельзя сложить")


    @property
    def number_of_sim(self):
        """
        Возвращает количество SIM-карт.
        :return: количество SIM-карт
        """
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value > 0:
            self.__number_of_sim = value
        else:
            raise ValueError("Количество SIM-карт должно быть больше нуля.")

class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price

    def __str__(self):
        return f"Name: {self.name}  |  Category: {self.category_name}  |  Price: {self.price} per unit"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.name == other.name and self.category_name == other.category_name and self.price == other.price
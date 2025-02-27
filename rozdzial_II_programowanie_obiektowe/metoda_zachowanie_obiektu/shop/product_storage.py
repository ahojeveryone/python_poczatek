class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price

    def describe_product(self):
        print(f"Name: {self.name}  |  Category: {self.category_name}  |  Price: {self.price} per unit")
class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price

def describe_product(product):
    print(f"Name: {product.name}  |  Category: {product.category_name}  |  Price: {product.price} per unit")
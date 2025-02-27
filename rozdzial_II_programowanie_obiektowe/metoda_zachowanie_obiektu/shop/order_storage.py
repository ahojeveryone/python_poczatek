import random
from .product_storage import Product

class OrderElement:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def count_element_price(self):
        return round(self.quantity * self.product.price, 2)

    def print_element(self):
        print(f"Order element: {self.product.name}  |  Category: {self.product.category_name}  |  Unit price: {self.product.price}  |  Quantity: {self.quantity}  |  Total price: {self.count_element_price()}")


class Order:
    def __init__(self, buyer_name, order_elements=None):
        self.buyer_name = buyer_name
        if order_elements is None:
            order_elements = []
        self.order_elements = order_elements

        total_price = self.count_total_price()
        self.total_price = total_price

    def count_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.count_element_price()
        return total_price

    def describe_order(self):
        print("=" * 40)
        if self.order_elements.__len__() == 0:
            print(f"There are no products ordered by {self.buyer_name}.")
        else:
            print(f"Items in the order purchased by {self.buyer_name}:")
            for product in self.order_elements:
                product.print_element()
            print(f"The cost of the order: {self.total_price}.")
        print("=" * 40)


def create_random_order():
    elements_number = random.randint(1, 20)
    elements = []
    for number in range(elements_number):
        element = OrderElement(Product(f"Product-{number+1}", f"Category-{random.randint(1,10)}", random.randint(1,300)/10), random.randint(1,10))
        elements.append(element)
    order = Order("Buyer Name", elements)
    return order
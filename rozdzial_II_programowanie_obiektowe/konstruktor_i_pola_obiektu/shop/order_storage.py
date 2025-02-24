import random
from .product_storage import Product
from .product_storage import describe_product

class Order:
    def __init__(self, buyer_name, products=None):
        self.buyer_name = buyer_name
        if products is None:
            products = []
        self.products = products

        total_price = 0
        total_price = count_total_price(products)
        self.total_price = total_price

def count_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price

def describe_order(order):
    print("=" * 20)
    if order.products.__len__() == 0:
        print(f"There are no products ordered by {order.buyer_name}.")
    else:
        print(f"Items in the order purchased by {order.buyer_name}:")
        for product in order.products:
            describe_product(product)
        print(f"The cost of the order: {order.total_price}.")
    print("=" * 20)

def create_random_order():
    products_number = random.randint(1, 20)
    products = []
    for number in range(products_number):
        product = Product(f"Product-{number+1}", f"Category-{random.randint(1,10)}", random.randint(1,300)/10)
        products.append(product)
    order = Order("Buyer Name", products)
    return order
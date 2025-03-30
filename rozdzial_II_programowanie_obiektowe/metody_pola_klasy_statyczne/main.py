import random
from shop.apple import Apple
from shop.potato import Potato
from shop.product_storage import Product
from shop.order_storage import Order, OrderElement
from shop.taxes import TaxCalculator


def run_homework_1():
    # order_1 = create_random_order(5)
    # print(order_1)

    order_2 = Order.create_random_order(15)
    print(order_2)

def run_homework_3():
    product = Product(name="New Product", category_name="FRUIT_VEGETABLE", price=random.randint(1, 300) / 10)
    order_element = OrderElement(product, quantity=random.randint(1, 10))

    print(order_element)
    print(f"Tax: {TaxCalculator.count_tax(order_element)}")

if __name__ == "__main__":
    run_homework_3()
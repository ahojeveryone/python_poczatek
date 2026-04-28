import random
from .order_element import OrderElement
from .product import Product
from .order import Order
from .product_category import *


MIN_QUANTITY = 1
MAX_QUANTITY = 5

MIN_PRICE = 1
MAX_PRICE = 14

MIN_IDENTIFIER = 1
MAX_IDENTIFIER = 10

def generate_order_elements(number_of_products=None):

    if number_of_products is None:
        number_of_products = random.randint(1,Order.MAX_ELEMENTS)

    order_elements = []
    for product_number in range(number_of_products):
        product_identifier = random.randint(MIN_IDENTIFIER,MAX_IDENTIFIER)
        product_name = f"Produkt-{product_number}"
        category_name = ProductCategory.OTHER
        unit_price = random.randint(MIN_PRICE, MAX_PRICE)
        product = Product(product_name, category_name, unit_price, product_identifier)
        quantity = random.randint(MIN_QUANTITY, MAX_QUANTITY)

        order_elements.append(OrderElement(product, quantity))



    return order_elements
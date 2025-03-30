import random
from itertools import product

from shop.product_storage import Product
from shop.order_storage import Order, OrderElement, create_random_order

def run_homework():
    order = create_random_order()
    print(order)

    print(30 * "=")

    #order_element = OrderElement(Product(f"New Product", f"New Category", random.randint(1,300)/10), random.randint(1,10))
    product = Product(name="New Product", category_name="New Category", price=random.randint(1,300)/10)
    order.add_new_element(product=product, quantity=random.randint(1,10))
    print(order)

if __name__ == "__main__":
    run_homework()
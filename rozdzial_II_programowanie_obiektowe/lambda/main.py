import random
from shop.apple import Apple
from shop.potato import Potato
from shop.product_storage import Product
from shop.order_storage import Order, OrderElement
from shop.taxes import TaxCalculator
from shop.discount_policy import Discount

def run_homework():

    orders = []
    for k in range(5):
        orders.append(Order.create_random_order(5, f"Buyer {k+1}"))
        # print("=" * 110)
        # print(f"ORDER NO. {k+1}")
        # print(orders[k])

    orders.sort(key=lambda order: order.count_total_price())
    print("Sorted orders:")
    for k in range(5):
        print(orders[k])

if __name__ == "__main__":
    run_homework()
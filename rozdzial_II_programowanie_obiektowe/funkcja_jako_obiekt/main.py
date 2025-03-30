import random
from shop.apple import Apple
from shop.potato import Potato
from shop.product_storage import Product
from shop.order_storage import Order, OrderElement
from shop.taxes import TaxCalculator
from shop.discount_policy import Discount

def say_hello(name):
    print(f"Hello {name}!")

def order_cost(order):
    return order.count_total_price()

def run_homework_1():

    orders = []
    for k in range(5):
        orders.append(Order.create_random_order(5, f"Buyer {k+1}"))
        print("=" * 110)
        print(f"ORDER NO. {k+1}")
        print(orders[k])

    orders.sort(key=order_cost)
    print("Sorted orders:")
    for k in range(5):
        print(orders[k])

def run_homework_2():

    # order_1 = Order.create_random_order(5, f"Buyer 1", Discount.festive_discount_policy)
    # print(order_1)
    #
    # order_2 = Order.create_random_order(5, f"Buyer 2", Discount.reg_customer_discount_policy)
    # print(order_2)
    #
    # order_3 = Order.create_random_order(1, f"Buyer 3", Discount.festive_discount_policy)
    # print(order_3)
    #
    # order_4 = Order.create_random_order(5, f"Buyer 4")
    # print(order_4)

    order_5 = Order.create_random_order(5, f"Buyer 5", Discount.festive_discount_policy)
    print(order_5)


if __name__ == "__main__":

    # say_hello("Agnes")
    # say_hi = say_hello
    # say_hi("Agnesita")

    #run_homework_1()
    run_homework_2()
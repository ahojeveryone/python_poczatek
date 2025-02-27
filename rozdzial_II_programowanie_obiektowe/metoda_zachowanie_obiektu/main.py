from shop.apple import Apple
from shop.potato import Potato
from shop.product_storage import Product
from shop.order_storage import Order, OrderElement, create_random_order

def run_homework_1():
    order = create_random_order()
    order.describe_order()

def run_homework_2():
    granny_smith = Apple("granny smith", "small", 3.40)
    print(f"Granny Smith apple: {granny_smith.name, granny_smith.size}")
    granny_smith.print_total_price(3)

    purple_majesty = Potato("purple majesty", "medium", 1.2)
    print(f"Purple Majesty potato: {purple_majesty.name, purple_majesty.size}")
    purple_majesty.print_total_price(10)

def run_homework_3():
    cookies = OrderElement(Product("cookies", "food", 4), 2)
    cookies.print_element()


if __name__ == "__main__":
    run_homework_1()
    # run_homework_2()
    # run_homework_3()
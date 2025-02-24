from shop.apple import Apple
from shop.potato import Potato
from shop.product_storage import Product, describe_product
from shop.order_storage import Order, create_random_order, describe_order

def run_homework():
    granny_smith = Apple("granny smith", "small", 3.40)
    jonagold = Apple("jonagold", "medium", 2.80)
    print(f"Granny Smith apple: {granny_smith.name}, {granny_smith.size}")
    print(f"Jonagold apple: {jonagold.name}, {jonagold.price_for_kilo}")

    purple_majesty = Potato("purple majesty", "medium", 1.2)
    print(f"Purple Majesty potato: {purple_majesty.name, purple_majesty}")

    cookies = Product("cookies", "food", 4)
    describe_product(cookies)
    apple = Product("red apple", "fruits", 1.20)
    describe_product(apple)

    empty_order = Order(buyer_name="Hannah Stocking")
    describe_order(empty_order)
    order_001 = Order("Eric Smith", [cookies, apple])
    describe_order(order_001)
    order = create_random_order()
    describe_order(order)

if __name__ == "__main__":
    run_homework()
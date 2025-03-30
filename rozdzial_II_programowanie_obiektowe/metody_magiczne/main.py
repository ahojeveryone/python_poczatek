from shop.apple import Apple
from shop.potato import Potato
from shop.product_storage import Product
from shop.order_storage import Order, OrderElement, create_random_order

def run_homework_1_3():
    order = create_random_order()
    print(order)

def run_homework_2():
    granny_smith = Apple("granny smith", "small", 3.40)
    print(granny_smith)

    purple_majesty = Potato("purple majesty", "medium", 1.2)
    print(purple_majesty)

def run_homework_4():
    cookies = Product("cookies", "food", 4)
    cookies_copy = Product("cookies", "food", 4)
    apple = Product("red apple", "fruits", 1.20)
    # print(cookies == apple)
    # print(cookies == cookies_copy)

    order_element_001 = OrderElement(product=cookies, quantity=1)
    order_element_002 = OrderElement(product=cookies, quantity=2)
    order_element_003 = OrderElement(product=cookies_copy, quantity=1)
    order_element_004 = OrderElement(product=apple, quantity=1)
    # print(f"Same product, different quantity: {order_element_001 == order_element_002}")
    # print(f"Same product, same quantity: {order_element_001 == order_element_003}")
    # print(f"Different product, same quantity: {order_element_001 == order_element_004}")

    order_001 = Order(buyer_name="Anna Nowak", order_elements=[order_element_001, order_element_002, order_element_003, order_element_004])
    order_002 = Order(buyer_name="Anna Nowak", order_elements=[order_element_001, order_element_002, order_element_003])
    order_003 = Order(buyer_name="Anna Kowalska", order_elements=[order_element_001, order_element_002, order_element_003])
    order_004 = Order(buyer_name="Anna Nowak", order_elements=[order_element_003, order_element_001, order_element_002])
    print(f"Same buyer, different products: {order_001 == order_002}")
    print(f"Same buyer, same products: {order_002 == order_004}")
    print(f"Different buyer, same products: {order_002 == order_003}")



if __name__ == "__main__":
    #run_homework_1_3()
    # run_homework_2()
    run_homework_4()
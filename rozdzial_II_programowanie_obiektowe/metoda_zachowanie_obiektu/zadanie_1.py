import random

class Product:
    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price

class Order:
    def __init__(self, buyer_name, products=None):
        self.buyer_name = buyer_name
        if products is None:
            products = []
        self.products = products

        total_price = 0
        total_price = count_total_price(products)
        self.total_price = total_price

class Apple:
    def __init__(self, name, size, price_for_kilo):
        self.price_for_kilo = price_for_kilo
        self.size = size
        self.name = name

class Potato:
    def __init__(self, name, size, price_for_kilo):
        self.price_for_kilo = price_for_kilo
        self.size = size
        self.name = name

def count_total_price(products):
    total_price = 0
    for product in products:
        total_price += product.price
    return total_price

def describe_product(product):
    print(f"Name: {product.name}  |  Category: {product.category_name}  |  Price: {product.price} per unit")

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
        product = Product(f"Product-{number}", f"Category-{random.randint(1,10)}", random.randint(1,300)/10)
        products.append(product)
    order = Order("Buyer Name", products)
    return order

def run_homework_2():
    granny_smith = Apple("granny smith", "small", 3.40)
    jonagold = Apple("jonagold", "medium", 2.80)
    # print(f"Granny Smith apple: {granny_smith.name}, {granny_smith.size}")
    # print(f"Jonagold apple: {jonagold.name}, {jonagold.price_for_kilo}")

    purple_majesty = Potato("purple majesty", "medium", 1.2)
    # print(f"Purple Majesty potato: {purple_majesty.name, purple_majesty}")

    cookies = Product("cookies", "food", 4)
    describe_product(cookies)
    apple = Product("red apple", "fruits", 1.20)
    describe_product(apple)

    empty_order = Order(buyer_name="Hannah Stocking")
    describe_order(empty_order)
    order_001 = Order("Eric Smith", [cookies, apple])
    describe_order(order_001)

def run_homework_3():
    order = create_random_order()
    describe_order(order)

if __name__ == "__main__":
    run_homework_3()

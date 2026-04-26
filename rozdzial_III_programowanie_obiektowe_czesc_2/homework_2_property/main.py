from shop.discount_policy import loyal_customer_policy, christmas_policy
from shop.order import Order
from shop.data_generator import generate_order_elements


def run_homework_1():
    first_name = "Mikołaj"
    last_name = "Lewandowski"
    order_elements = generate_order_elements(8)
    order = Order(first_name, last_name, order_elements)

    print("Elementy wylistowane przy użyciu gettera:")
    for element in order.order_elements:
        print(element)

def run_homework_2():
    first_name = "Mikołaj"
    last_name = "Lewandowski"
    order_elements = generate_order_elements(9)
    order = Order(first_name, last_name, order_elements)

    print("Zamówienie pierwotne:")
    print(order)

    new_order_elements = generate_order_elements(5)
    order.order_elements = new_order_elements

    print("Zamówienie zmienione:")
    print(order)

if __name__ == '__main__':
    run_homework_2()

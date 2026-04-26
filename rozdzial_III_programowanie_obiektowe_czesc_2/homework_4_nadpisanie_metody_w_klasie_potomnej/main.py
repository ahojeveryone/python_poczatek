from shop.data_generator import generate_order_elements
from shop.order import Order
from shop.express_order import ExpressOrder


def run_homework():

        order_elements = generate_order_elements(4)

        normal_order = Order(
            client_first_name="Mateusz",
            client_last_name="Nowak",
            order_elements=order_elements)
        print(normal_order)

        express_order = ExpressOrder(
            client_first_name="Mateusz",
            client_last_name="Nowak",
            order_elements=order_elements,
            shipment_date="03-04-2025")
        print(express_order)


if __name__ == '__main__':
    run_homework()

from shop.data_generator import generate_order_elements
from shop.order import Order
from shop.express_order import ExpressOrder
from shop.discount_policy import DiscountPolicy, PercentageDiscount, AbsoluteDiscount


def run_homework():

        order_elements = generate_order_elements(4)

        normal_order = Order(
            client_first_name="Normal",
            client_last_name="Client",
            order_elements=order_elements,
            discount_policy=DiscountPolicy())
        print(normal_order)

        order_with_perc_discount = Order(
            client_first_name="Percentage Discount",
            client_last_name="Client",
            order_elements=order_elements,
            discount_policy=PercentageDiscount(5))
        print(order_with_perc_discount)

        order_with_absolute_discount = Order(
            client_first_name="Absolute Discount",
            client_last_name="Client",
            order_elements=order_elements,
            discount_policy=AbsoluteDiscount(20))
        print(order_with_absolute_discount)


if __name__ == '__main__':
    run_homework()

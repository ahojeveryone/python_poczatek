from shop.data_generator import generate_order_elements
from shop.order import Order
from shop.express_order import ExpressOrder
from shop.discount_policy import DiscountPolicy, PercentageDiscount, AbsoluteDiscount


def run_homework():

        order_elements = generate_order_elements()
        identifier_to_product = {element.product.identifier: element.product  for element in order_elements}
        print(identifier_to_product)

        identifier_to_product_increased = {
            identifier+1: product
            for identifier, product in identifier_to_product.items()
        }
        print(identifier_to_product_increased)

        identifier_to_product_joined = identifier_to_product.copy()
        identifier_to_product_joined.update(identifier_to_product_increased)
        print(identifier_to_product_joined)

if __name__ == '__main__':
    run_homework()

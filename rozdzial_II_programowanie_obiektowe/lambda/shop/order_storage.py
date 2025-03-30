import random
from .product_storage import Product
from .discount_policy import Discount

class OrderElement:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = self.count_element_price()

    def __str__(self):
        return f"Order element: {self.product.name}  |  Category: {self.product.category_name}  |  Unit price: {self.product.price}  |  Quantity: {self.quantity}  |  Total price: {self.total_price}"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product == other.product and self.quantity == other.quantity

    def count_element_price(self):
        return round(self.quantity * self.product.price, 2)


class Order:

    MAX_ORDER_ELEMENTS_NUMBER = 10

    def __init__(self, buyer_name, order_elements=None, discount_policy=None):
        self.buyer_name = buyer_name
        if order_elements is None:
            order_elements = []
        if len(order_elements) > Order.MAX_ORDER_ELEMENTS_NUMBER:
            order_elements = order_elements[:Order.MAX_ORDER_ELEMENTS_NUMBER]
        self.order_elements = order_elements

        # total_price = self.count_total_price()
        # discount_price = self.count_price_after_discount()
        # if discount_policy == Discount.festive_discount_policy:
        #     discount_price = Discount.festive_discount_policy(total_price)
        # elif discount_policy == Discount.reg_customer_discount_policy:
        #     discount_price = Discount.reg_customer_discount_policy(total_price)

        # self.total_price = total_price
        #self.discount_price = self.count_price_after_discount(discount_policy)

    def __str__(self, discount_policy=None):
        mark_line = "=" * 110
        if len(self) == 0:
            personal_details = f"There are no products ordered by {self.buyer_name}."
        else:
            personal_details = f"List of {len(self)} items in the order purchased by {self.buyer_name}:"
            product_details = ""
            for element in self.order_elements:
                product_details += f"\t{element}\n"
            value_details = f"The cost of the order: {self.count_price_after_discount(discount_policy)} (before discount: {self.count_total_price()})."
        result = "\n".join([mark_line, personal_details, product_details]) + value_details
        return result

    def __len__(self):
        return len(self.order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.buyer_name != other.buyer_name:
            return False
        if  len(self) != len(other):
            return False
        for element in self.order_elements:
            if element not in other.order_elements:
                return False
        return True

    def count_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.count_element_price()
        return round(total_price, 2)

    def count_price_after_discount(self, discount_policy):
        discount_price = self.count_total_price()
        if discount_policy == Discount.festive_discount_policy:
            discount_price = Discount.festive_discount_policy(discount_price)
        elif discount_policy == Discount.reg_customer_discount_policy:
            discount_price = Discount.reg_customer_discount_policy(discount_price)
        return round(discount_price, 2)

    @classmethod
    def create_random_order(cls, elements_number, buyer_name, discount_policy=None):
        #elements_number = random.randint(1, 20)
        elements = []
        for number in range(elements_number):

            element = OrderElement(Product(f"Product-{number+1}", f"Category-{random.randint(1,10)}", random.randint(1,300)/10), random.randint(1,10))
            if len(elements) >= cls.MAX_ORDER_ELEMENTS_NUMBER:
                print("You have reached the maximum number of elements in the order. You cannot add anything else.")
                break
            elements.append(element)

        order = Order(buyer_name, elements, discount_policy)
        return order
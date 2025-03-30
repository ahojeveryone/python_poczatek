import random
from .product_storage import Product

class OrderElement:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        return f"Order element: {self.product.name}  |  Category: {self.product.category_name}  |  Unit price: {self.product.price}  |  Quantity: {self.quantity}  |  Total price: {self.count_element_price()}"

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        return self.product == other.product and self.quantity == other.quantity

    def count_element_price(self):
        return round(self.quantity * self.product.price, 2)


class Order:
    def __init__(self, buyer_name, order_elements=None):
        self.buyer_name = buyer_name
        if order_elements is None:
            _order_elements = []
        self._order_elements = order_elements

        total_price = self._count_total_price()
        self.total_price = total_price

    def __str__(self):
        mark_line = "=" * 110
        if len(self) == 0:
            personal_details = f"There are no products ordered by {self.buyer_name}."
        else:
            personal_details = f"List of {len(self)} items in the order purchased by {self.buyer_name}:"
            product_details = ""
            for element in self._order_elements:
                product_details += f"\t{element}\n"
            value_details = f"The cost of the order: {self.total_price}."
        result = "\n".join([mark_line, personal_details, product_details]) + value_details
        return result

    def __len__(self):
        return len(self._order_elements)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return NotImplemented
        if self.buyer_name != other.buyer_name:
            return False
        if  len(self) != len(other):
            return False
        for element in self._order_elements:
            if element not in other._order_elements:
                return False
        return True

    def _count_total_price(self):
        total_price = 0
        for element in self._order_elements:
            total_price += element.count_element_price()
        return round(total_price, 2)

    def add_new_element(self, product, quantity):
        element = OrderElement(product, quantity)
        self._order_elements.append(element)
        # self.total_price += element.count_element_price()
        self.total_price = self._count_total_price()

def create_random_order():
    elements_number = random.randint(1, 20)
    elements = []
    for number in range(elements_number):
        element = OrderElement(Product(f"Product-{number+1}", f"Category-{random.randint(1,10)}", random.randint(1,300)/10), random.randint(1,10))
        elements.append(element)
    order = Order("Buyer Name", elements)
    return order
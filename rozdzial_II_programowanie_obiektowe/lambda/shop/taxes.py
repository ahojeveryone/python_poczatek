from .order_storage import Order, OrderElement

class TaxRates:

    FRUIT_VEGETABLE_TAX = 0.05
    FOOD_TAX = 0.08
    OTHER_PRODUCTS_TAX = 0.2


class TaxCalculator:

    @staticmethod
    def count_tax(order_element):
        product_category = order_element.product.category_name
        if product_category == "FRUIT_VEGETABLE":
            tax_rate = TaxRates.FRUIT_VEGETABLE_TAX
        elif product_category == "FOOD_TAX":
            tax_rate = TaxRates.FOOD_TAX
        else:
            tax_rate = TaxRates.OTHER_PRODUCTS_TAX
        return round(order_element.total_price * tax_rate, 2)
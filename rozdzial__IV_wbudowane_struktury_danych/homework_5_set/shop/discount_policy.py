class DiscountPolicy:

    def apply_discount(self, total_price):
        return total_price

class PercentageDiscount(DiscountPolicy):

    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def apply_discount(self, total_price):
        return total_price * (100 - self.discount_percentage) / 100

class AbsoluteDiscount(DiscountPolicy):

    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, total_price):
        if total_price > self.discount_amount:
            return total_price - self.discount_amount
        return 0


# def default_policy(total_price):
#     return total_price
#
#
# def loyal_customer_policy(total_price):
#     return 0.95 * total_price
#
#
# def christmas_policy(total_price):
#     if total_price > 100:
#         return total_price - 20
#     return total_price

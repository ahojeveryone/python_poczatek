class Discount:

    def default_price(total_price):
        return total_price

    def reg_customer_discount_policy(total_price):
        return round(total_price * 0.95, 2)

    def festive_discount_policy(total_price):
        if total_price > 100:
            total_price -= 20
        return total_price

import datetime
from xmlrpc.client import DateTime

from shop.product import ExpiringProduct


def run_homework():

    products = []

    good_product = ExpiringProduct(name="chips", category_name="snacks", unit_price=1.30, production_year=2024, validity_years=3)
    products.append(good_product)
    expired_product = ExpiringProduct(name="chips", category_name="snacks", unit_price=1.20, production_year=2020, validity_years=3)
    products.append(expired_product)

    current_year = datetime.date.today().year
    print(f"Obecny rok to: {current_year}")
    for product in products:
        if product.does_expire(current_year):
            print(f"{product} <-- przeterminowany")
        else:
            print(f"{product} <-- zdatny do spożycia")



if __name__ == '__main__':
    run_homework()

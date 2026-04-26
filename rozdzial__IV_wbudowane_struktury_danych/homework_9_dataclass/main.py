from shop.product import Product
from shop.order_element import OrderElement
from shop.expiring_product import *

def run_homework():
        base_product = Product(name="jezyki", category_name="cookies and sweets", unit_price=8.7)
        same_product = Product(name="jezyki", category_name="cookies and sweets", unit_price=8.7)
        diff_name_product = Product(name="delicje", category_name="cookies and sweets", unit_price=8.7)
        diff_cat_name_product = Product(name="jezyki", category_name="cookies", unit_price=8.7)
        diff_price_product = Product(name="jezyki", category_name="cookies and sweets", unit_price=8.8)
        # print(base_product)
        # print(base_product.__eq__(same_product))
        # print(base_product.__eq__(diff_name_product))
        # print(base_product.__eq__(diff_cat_name_product))
        # print(base_product.__eq__(diff_price_product))
        # print(base_product.__eq__("abc"))

        first_order = OrderElement(base_product, 10)
        second_order = OrderElement(base_product, 10)
        third_order = OrderElement(base_product, 11)
        fourth_order = OrderElement(diff_name_product, 10)
        # print(first_order)
        # print(first_order.__eq__(second_order))
        # print(first_order.__eq__(third_order))
        # print(first_order.__eq__(fourth_order))
        # print(first_order.calculate_price())

        good_product = ExpiringProduct(name="jezyki", category_name="cookies and sweets", unit_price=8.7, production_year=2026, validity_years=2)
        expired_product = ExpiringProduct(name="jezyki", category_name="cookies and sweets", unit_price=8.7,
                                       production_year=2021, validity_years=2)
        print(good_product)
        print(good_product.does_expire())
        print(expired_product)
        print(expired_product.does_expire())
        print(good_product.__eq__(expired_product))

if __name__ == '__main__':
    run_homework()

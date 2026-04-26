from collections import namedtuple
from zoneinfo import available_timezones

from shop.product import Product

# homework 7 (tuple)
def test_check_eq_function():

        # base_product = Product(
        #         identifier=1,
        #         name="base_product",
        #         category_name="category1",
        #         unit_price=1
        # )
        #
        # duplicated_product = base_product
        #
        # diff_id_product = Product(
        #         identifier=2,
        #         name="base_product",
        #         category_name="category1",
        #         unit_price=1
        # )
        #
        # diff_name_product = Product(
        #         identifier=1,
        #         name="additional_product",
        #         category_name="category1",
        #         unit_price=1
        # )
        #
        # diff_category_product = Product(
        #         identifier=1,
        #         name="base_product",
        #         category_name="category2",
        #         unit_price=1
        # )
        #
        # diff_price_product = Product(
        #         identifier=1,
        #         name="base_product",
        #         category_name="category1",
        #         unit_price=1.4
        # )
        #
        # same_price_product = Product(
        #         identifier=1,
        #         name="base_product",
        #         category_name="category1",
        #         unit_price=1.4
        # )
        #
        # parameters = [
        #         (base_product, duplicated_product, True),
        #         (base_product, diff_id_product, False),
        #         (base_product, diff_name_product, False),
        #         (base_product, diff_category_product, False),
        #         (base_product, diff_price_product, False),
        #         (diff_category_product, diff_price_product, False),
        #         (diff_price_product, same_price_product, True)
        # ]

        parameters = [
                ("Ciastka", "Jedzenie", 4, "Ciastka", "Jedzenie", 4, True),
                ("Ciastka", "Jedzenie", 4, "Chleb", "Jedzenie", 4, False),
                ("Ciastka", "Jedzenie", 4, "Ciastka", "Słodycze", 4, False),
                ("Ciastka", "Jedzenie", 4, "Ciastka", "Jedzenie", 5, False)
        ]

        for params in parameters:
                name, category, price, other_name, other_category, other_price, expected_result = params
                result = Product(name, category, price) == Product(other_name, other_category, other_price)

                if result == expected_result:
                        print("OK")
                else:
                        print(f"Błąd! Dla danych: {params} wynik porównania to {result} zamiast {expected_result}")

def run_test():
        test_check_eq_function()

# homework 8 (named tuple)
AppleTuple = namedtuple("AppleTuple", ["species_name", "size", "price"])

def run_homework_namedtuple():
        apple = AppleTuple("granny smith", "medium", 6.70)
        print(f"[PKT. A - NAZWY] species name: {apple.species_name}, size: {apple.size}, price: {apple.price}")
        print(f"[PKT. B - INDEKSY] species name: {apple[0]}, size: {apple[1]}, price: {apple[2]}")
        print("[PKT C - PĘTLA]")
        for detail in apple:
                print(detail)

if __name__ == '__main__':
    #run_test()
    run_homework_namedtuple()

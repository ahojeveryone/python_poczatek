from zoneinfo import available_timezones

from shop.products_delivery import products_delivery, AVAILABLE_PRODUCTS

def run_homework():
        needed_products = AVAILABLE_PRODUCTS
        received_products = []

        while not set(needed_products) == set(received_products):
                new_products = products_delivery()
                received_products += new_products
                print(f"Otrzymano: {new_products}")
                missing_products = set(needed_products).difference(received_products)
                print(f"Brakuje nam jeszcze: {missing_products}")

        print(f"Łącznie otrzymano: {received_products}")

if __name__ == '__main__':
    run_homework()

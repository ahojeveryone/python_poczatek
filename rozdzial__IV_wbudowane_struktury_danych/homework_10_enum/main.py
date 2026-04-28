from shop.product_category import *
from shop.product import *
from shop.data_generator import *

def run_homework():
        # print("enum without auto")
        # print(ProductCategory.FOOD)
        # print(ProductCategory.DRINKS.name)
        # print(ProductCategory.JEWELERY.value)
        #
        # print("enum with auto")
        # print(ProductCategoryNames.FOOD)
        # print(ProductCategoryNames.DRINKS.name)
        # print(ProductCategoryNames.JEWELERY.value)

        base_product = Product(name="jezyki", category_name=ProductCategory.FOOD, unit_price=8.7, product_identifier=1)
        print(base_product)

        order = generate_order_elements(10)
        for k in range(order.__len__()):
                print(order[k])

if __name__ == '__main__':
    run_homework()

from enum import Enum, auto

class ProductCategory(Enum):
    FOOD = "Jedzenie"
    DRINKS = "Napoje"
    JEWELERY = "Biżuteria"
    CHEMICALS = "Chemia gospodarcza"

class NamedProductCategory(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class ProductCategoryNames(NamedProductCategory):
    FOOD = auto()
    DRINKS = auto()
    JEWELERY = auto()
    CHEMICALS = auto()

def run_homework():
    print("enum without auto")
    print(ProductCategory.FOOD)
    print(ProductCategory.DRINKS.name)
    print(ProductCategory.JEWELERY.value)

    print("enum with auto")
    print(ProductCategoryNames.FOOD)
    print(ProductCategoryNames.DRINKS.name)
    print(ProductCategoryNames.JEWELERY.value)

if __name__ == '__main__':
    run_homework()
from enum import Enum, auto

class ProductCategory(Enum):
    FOOD = "Jedzenie"
    DRINKS = "Napoje"
    JEWELERY = "Biżuteria"
    CHEMICALS = "Chemia gospodarcza"
    OTHER = "Inne"

class NamedProductCategory(Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

class ProductCategoryNames(NamedProductCategory):
    FOOD = auto()
    DRINKS = auto()
    JEWELERY = auto()
    CHEMICALS = auto()
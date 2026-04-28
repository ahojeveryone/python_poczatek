from dataclasses import dataclass
from .product_category import *

@dataclass
class Product:
    name: str
    category_name: ProductCategory
    unit_price: float
    product_identifier: int

    # def __eq__(self, other):
    #     if self.__class__ != other.__class__:
    #         return NotImplemented
    #     return (self.name == other.name and
    #             self.category_name == other.category_name and
    #             self.unit_price == other.unit_price)

    def __str__(self):
        return f"Nazwa: {self.name} | Kategoria: {self.category_name.value} | Cena: {self.unit_price} PLN/szt"



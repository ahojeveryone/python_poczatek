import datetime
from dataclasses import dataclass
from .product import Product

@dataclass
class ExpiringProduct(Product):
    production_year: int
    validity_years: int

    # def __init__(self, production_year, validity_years, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.production_year = production_year
    #     self.validity_years = validity_years

    def does_expire(self):
        return datetime.datetime.now().year > self.production_year + self.validity_years

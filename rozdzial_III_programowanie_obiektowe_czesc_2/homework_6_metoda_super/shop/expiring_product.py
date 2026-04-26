from .product import Product


class ExpiringProduct(Product):

    def __init__(self, production_year, validity_years, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.production_year = production_year
        self.validity_years = validity_years

    def does_expire(self, current_year):
        return current_year > self.production_year + self.validity_years

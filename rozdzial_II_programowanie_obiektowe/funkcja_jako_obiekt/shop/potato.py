class Potato:
    def __init__(self, name, size, price_for_kilo):
        self.price_for_kilo = price_for_kilo
        self.size = size
        self.name = name

    def __repr__(self):
        return f"<Potato name={self.name}, size={self.size}, price_for_kilo={self.price_for_kilo}>"

    def count_total_price(self, kilos):
        return kilos * self.price_for_kilo

    def print_total_price(self, kilos):
        print(f"The cost of {kilos} kilograms of {self.name} = {self.count_total_price(kilos)}")
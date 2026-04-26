from .order import Order


class ExpressOrder(Order):
    EXPRESS_ORDER_FEE = 10

    def __init__(self, shipment_date, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shipment_date = shipment_date

    @property
    def total_price(self):
        return super().total_price + ExpressOrder.EXPRESS_ORDER_FEE

    def __str__(self):
        mark_line = "-" * 20
        order_details = f"Zamówienie złożone przez: {self.client_first_name} {self.client_last_name}"
        value_details = f"O łącznej wartości: {self.total_price} PLN"
        normal_order_value = f"Łączna wartość zamówionych produktów: {super().total_price} PLN"
        express_order_fee = f"Dodatkowa opłata za ekspresową przesyłkę: {ExpressOrder.EXPRESS_ORDER_FEE} PLN"
        shipment_date = f"Data dostawy: {self.shipment_date}"
        product_details = "Zamówione produkty:\n"
        for element in self._order_elements:
            product_details += f"\t{element}\n"
        result = "\n".join(
            [mark_line, order_details, value_details, normal_order_value, express_order_fee, shipment_date, product_details,
             mark_line])
        return result

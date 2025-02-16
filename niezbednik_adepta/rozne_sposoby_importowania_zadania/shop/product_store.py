current_stock = {
    "bread":
        {
            "quantity": 10,
            "price": 2.5
        },
    "apples": {
            "quantity": 30,
            "price": 1.6
        },
    "eggs": {
            "quantity": 15,
            "price": 1
        },
    "carrots": {
            "quantity": 50,
            "price": 0.5
        },
}


def update_product_quantity(product_name, product_quantity):
    current_stock[product_name]["quantity"] -= product_quantity
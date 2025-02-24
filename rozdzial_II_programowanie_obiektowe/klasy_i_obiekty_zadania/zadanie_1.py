class Produkt:
    pass


class Order:
    pass


class Apple:
    pass

class Potato:
    pass


if __name__ == "__main__":
    jablko_reneta = Apple()
    jablko_ligol = Apple()
    ziemniak_irga = Potato()

    print(f"Type of jablko_reneta: {type(jablko_reneta)}")
    print(f"Type of jablko_ligol: {type(jablko_ligol)}")
    print(f"Type of ziemniak_irga: {type(ziemniak_irga)}")

    # orders = [Order(), Order(), Order(), Order(), Order()]
    orders = []
    for _ in range(5):
        orders.append(Order())
    print(orders)

    types_of_products = {
        "jablko": Produkt(),
        "ziemniak": Produkt()
    }
    print(types_of_products)
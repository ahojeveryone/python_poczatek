from .product_store import current_stock, update_product_quantity

shopping_list = []

def add_item_to_shopping_list(item, quantity):
    if item not in current_stock:
        print("You have chosen a product that is not in our inventory")
    else:
        if current_stock[item]["quantity"] < quantity:
            print("We don't have the qauntity you want.")
        else:
            cost = quantity * current_stock[item]["price"]
            print(f"Total price of the purchased product equals: {cost}$.")
            new_order = {
                "product": item,
                "quantity": quantity,
                "total_price": cost
            }
            shopping_list.append(new_order)
            update_product_quantity(item, quantity)
            return new_order





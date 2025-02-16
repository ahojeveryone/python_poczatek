from shop.purchase_order import add_item_to_shopping_list

def run_creating_purchase():
    chosen_item = None
    while chosen_item != "X":
        chosen_item = input("What item would you like to purchase? If none, press X. ")

        if chosen_item.upper() == "X":
            break
        chosen_quantity = int(input("How much/many? "))

        result = add_item_to_shopping_list(chosen_item, chosen_quantity)

if __name__ == "__main__":
    run_creating_purchase()




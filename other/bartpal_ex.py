if __name__ == '__main__':

    raw = {
    "data": {
        "command": "PlaceOrder",
        "requestor": "sys://users/1",
        "basket": [
            {
                "SKU": "sys://items/food/pizza/18",
                "name": "Pizza Margherita",
                "qty": 1
            },
            {
                "SKU": "sys://items/food/salads/21",
                "name": "Cesar Salad",
                "qty": 1
            },
            {
                "SKU": "sys://items/food/pizza/91",
                "name": "Pizza Diavola",
                "qty": 2
            }
        ],
        "customizations": {
            "sys://items/food/pizza/91": [
                {
                    "type": "AddIngredient",
                    "ingredient": "Jalapeno",
                    "qty": 3
                },
                {
                    "type": "AllergyRestriction",
                    "allergy": "peanuts",
                    "severity": "HIGH"
                }
            ],
            "sys://items/food/salads/21": [
                {
                    "type": "AllergyRestriction",
                    "allergy": "lactose",
                    "severity": "CRITICAL"
                }
            ]
        },
        "metadata": {
            "trace_id": "123",
            "request_id": "456"
        }
    }
}

    allergy_counter = 0

    for customization, custom_details in raw["data"]["customizations"].items():
        for detail in custom_details:
            if detail["type"] == "AllergyRestriction" and (detail["severity"] == "HIGH" or detail["severity"] == "CRITICAL"):
                for item in raw["data"]["basket"]:
                    if item["SKU"] == customization:
                        allergy_counter += item["qty"]

    print("Total quantity of items, for which the user reported an allergy restriction with a severity of HIGH or CRITICAL: ", allergy_counter)
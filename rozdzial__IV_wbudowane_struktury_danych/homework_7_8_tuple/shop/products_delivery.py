import random

AVAILABLE_PRODUCTS = [
    "chleb",
    "ciastka",
    "jabłka",
    "dżem",
    "pomarańcze",
    "marchew",
    "bułki",
    "ziemniaki",
    "ser",
    "mleko"
]

def products_delivery():
    return [AVAILABLE_PRODUCTS[random.randint(0,9)] for _ in range(5)]
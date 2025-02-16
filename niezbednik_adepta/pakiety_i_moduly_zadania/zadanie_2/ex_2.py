# Zadanie nr 2
# Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta na podstawie otrzymanych długości przyprostokątnych.
# Wykorzystaj w tym celu moduł math z biblioteki standardowej

import math

def calculate_c_len(a_len, b_len):
    return math.sqrt(math.pow(a_len,2) + math.pow(b_len,2))

a = float(input("Give the length of the first cathetus: "))
b = float(input("Give the length of the second one: "))

c = calculate_c_len(a, b)
print(f"The length of hypotenuse equals: {c}")
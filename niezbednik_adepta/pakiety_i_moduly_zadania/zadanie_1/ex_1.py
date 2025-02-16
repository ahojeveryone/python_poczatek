# Zadanie nr 1
# Napisz funkcję obliczającą średnią prędkość biegu na podstawie czasu i pokonanego dystansu (prędkość = dystans / czas) i umieść ją w jednym pliku.
#
# W drugim pliku zaimportuj moduł, wczytaj informacje od użytkownika i wywołaj funkcję - oblicz prędkość średnią.

import speed_calculator
from speed_calculator import avg_speed

kilometers = float(input("How many kilometers have you carried? "))
hours = float(input("How many hours have it taken? "))

if (hours > 0 and kilometers >=0):
    avg_speed = speed_calculator.avg_speed(kilometers, hours)
    print(f"You have driven with the speed {avg_speed} km per hour.")
else:
    print("The input data was wrong.")
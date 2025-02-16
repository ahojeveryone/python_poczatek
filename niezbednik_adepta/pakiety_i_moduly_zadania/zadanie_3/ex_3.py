# Napisz kalkulator obliczający wartość lokaty po pewnym czasie.
# Wczytaj od użytkownika informacje o:
# - Początkowym kapitale (wpłaconej kwocie)
# - Oprocentowaniu
# - Okresie trwania inwestycji (w latach)
# Umieść funkcję obliczająca wartość lokaty w pakiecie calculations, a wczytanie danych i uruchomienie obliczeń w pliku powyżej pakietu.


# import calculations.investement
# from calculations import investement
from calculations.investement import net_present_value


def ask_for_parameters(message):
    return float(input(message))

print("Calculator counting net present value of a deposit.")
init_capital = ask_for_parameters("How much money have you put into the deposit? ")
yearly_rate = ask_for_parameters("What was the yearly rate (%)? ")
period = ask_for_parameters("What was the period (in years)? ")

value = net_present_value(init_capital, yearly_rate, period)
print(f"Net present value of the deposit after {period} years is equal to: {value:.2f}")

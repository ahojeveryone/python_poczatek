### Intro
Parsowanie zmiennych: np. ```float()```, ```int()```

Printowanie tekstu na konsoli z wykorzystaniem zmiennej: ```print(f"Put a value {value} into text.")```

Printowanie float z dokładnością do 2 miejsc po przecinku: ```print(f"Approx value: {value:.2f}")```

Pobieranie inputu z konsoli po wyświetleniu tekstu: ```input("Give me a value of sth: ")```

## IMPORT
Definiowanie co ma być zaimportowane z pakietu jeśli zrobimy ```import*``` : w pliku ___init__.py_ definiujemy
```__all__=["module_1","module_2",…]``` lub importujemy pakiety do tego pliku.

Zmiana nazwy importowanego pakietu (przy odnoszeniu się do niego w kodzie): ```from ... import ... as ...```

Zaimportowanie (względne) modułu z pakietu, w którym obecnie jesteśmy: ```from .[...]  import ...```

Importowanie względne stosujemy tylko wewnątrz pakietu. W pozostały miejscach korzystamy tylko z importowania bezwzględnego.

## Git
**Git** - system kontroli wersji instalowany jako program na komputerze

**GitHub** – platforma hostingowa dla projektów korzystających z Gita

### Nowe repozytorium, commit i push
1. Otwieramy w wybranym katalogu Git Bash
2. Rozpoczynamy repozytorium komendą ```git init```
3. Dodajemy niepotrzebne pliki do pliku _.gitignore_, np. _.idea/   *.pyc_ 
4. Dodajemy wszystkie pliki do repo komendą ```git add-A``` oraz ```git commit-m "Commit description"```
5. Inicjujemy połączenie repo lokalnego ze zdalnym: ```git remote add origin http://...```
6. Wypychamy pliki: ```git push-u origin master```

### Kolejne commity
1. Wykonujemy zmiany
2. Dodajemy zmiany do lokalnego repo  git add-A oraz git commit-m "Opis commita"
3. Wypychamy zmiany  git push


## PROGRAMOWANIE PROJEKTOWE
Paradygmat programowania = styl programowania 

**Paradygmaty programowania**: 
- **Deklaratywny** – definiujemy efekt, który chcemy uzyskać, a nie to jak do tego dojść (SQL)
- **Imperatywny** – dokładne definiowanie przepływu programu i sekwencji komend do wykonania (Python)
- <ins>**Proceduralny**</ins> – programowanie imperatywne wykorzystujące reużywalne procedury (Python, jeśli użyjemy funkcji)
- <ins>**Obiektowy**</ins> – zbiór obiektów, które komunikują się wzajemnie oraz mają pewne cechy i zachowania (Python)
- **Funkcyjny** – program zbudowany za pomocą bezstanowych funkcji
- **Aspektowy** – pozwala na obsłużenie przecinających się konceptów, np. sprawdzenie czy użytkownik jest zalogowany przed wykonaniem każdej funkcji w systemie
- **Zdarzeniowy** – programowanie oparte o emisję i nasłuchiwanie zdarzeń, zazwyczaj w sposób asynchroniczny (JavaScript)

## Programowanie obiektowe
KLASA = STRUKTURA STANU (dane dot. obiektu) + ZACHOWANIE (metody; metoda jest szczególnym przypadkiem funkcji)

OBIEKT = przykład elementu klasy

Klasa definiuje nowy typ w programie

**Koncepcje**:
- **Enkapsulacja** – prawo do prywatności
- **Abstrakcja** – możliwość definiowania poszczególnych elementów w sposób ogólny, bez podawania szczegółów
- **Dziedziczenie** – możliwość dziedziczenia cech innych obiektów
- **Kompozycja** – możliwość zawierania w sobie czegoś/ bycia częścią czegoś
- **Polimorfizm** – nie przejmowanie się jakie typu jest dany obiekt

| Co nazywamy    | Przykład                 | Nazwa konwencji | 
|----------------|--------------------------|-----------------|
| zmienne        | best_students = ...      | snake_case      |    
| stałe          | MAX_GRADE = ...          | MACRO_CASE      |
| funkcje/metody | def calculate_results(): | snake_case      |
| klasy          | class StudentAddress:    | PascalCase      |
| pliki          | product_store.py         | snake_case      |



### Konstruktor
- konstruktor zostaje wywołany automatycznie podczas tworzenia nowego obiektu
- cel: definicja i inicjalizacja stanu obiektu
```python
def __init__(self, nazwa_cechy):
    self.nazwa_cechy = "xyz"
```

### Magic methods / dunder (double underscore)
```__init__ ```
- konstruktor

```__str__ ```
- słowna reprezentacja obiektu
- musi zwracać typ string lub f-string
- służy uproszczonemu opisowi obiektu
- jeżeli mamy zdefiniowaną metodę ```__str__ ```, to zostanie ona domyślnie wykorzystana jeśli użyjemy ```print(nazwa_obiektu)```
- jeśli nie zdefiniujemy metody ```__str__ ```, Python domyślnie użyje metody ```__str__ ```
- 
```__str__ ```
- oficjalna tekstowa reprezentacja obiektu
- powinna zawierać wszelkie użyteczne informacje
- w przypadku braku zdefiniowania metody, Python użyje domyślnej implementacji
- dobrze opis dawać w nawiasach ```< ... >```

`__int__` oraz ```__float__```
- liczbowa reprezentacja obiektu
- brak domyślnej implementacji w Pythonie

```__len__```
- zwraca liczbę całkowitą nieujemną reprezentującą długość danego obiektu, o ile takie pojęcie ma sens w kontekście danej klasy

```__bool__```
- reprezentacja obiektu przez typ bool
- domyślnie Python zwróci metodę ```__len__```, czyli zwróci ```False``` jeśli długość ```0``` oraz ```True``` w p.p.
- jeśli brakuje implementacji metody ```__len__```, to ```__bool__``` zawsze zwróci ```True```

```__add__```, ```__sub__```, ```__mul__``` oraz ```__truediv__```
- zwracają wynik działania odpowiedniego operatora ```+```, ```-```, ```*``` oraz ```:```
- przyjmują dwa argumenty: ```(self, other)```

`__eq__`, `__ne__`, `__gt__` oraz `__lt__`
- operatory porównania, zwracają warości `True`, `False` albo `NotImplemented`
- przyjmują dwa argumenty: `(self, other)`

| Operator porównania   | Metoda    |
|-----------------------|-----------|
| `==`                  | `__eq__`  |
| `!=`                  | `__ne__`  |
| `<`                   | `__lt__`  |
| `<=`                  | `__le__`  |
| `>`                   | `__gt__`  |
| `>=`                  | `__ge__`  |


`__class__`
- zwraca klasę obiektu
- użycie: `obiekt.__class__`


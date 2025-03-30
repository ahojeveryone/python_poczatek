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
- **Enkapsulacja** – prawo do prywatności - dzięki niemu stan obiektu może zostać zmodyfikowany jedynie poprzez wywołanie funkcji na tymże obiekcie (a więc pośrednio); obiektów z zewnątrz nie interesuje w jaki sposób zmienia się zestaw danych, a jedynie jakie dane są przez ten obiekt dostarczane (zachowanie jest dla nas **abstrakcyjne**); dzięki temu usunikamy kaskadowego nanoszenia zmian; 
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

### Enkapsulacja 
Mamy dwie metody wprowadzenia enkapsulacji w Pythonie:
1. zmienne/funkcje, które mają być prywatne definiujemy w konstruktorze dodając do nazwy znak _ i używamy ich tylko wewnątrz klasy, tj.
``` python
class Student:

    def __init__(self):
        self._private_value = 7
        self.normal_value = 35
       
    def _private_function(self):
        ...
```
Jeśli użyjemy ich na zewnątrz, to Python zwróci nam odpowiedni komuniakt ostrzegający (ale wszystko się i tak wykona).
2. zmienne/funkcje, które mają być prywatne definiujemy w konstruktorze dodając do nazwy znak __ - tych nie można już użyć na zewnątrz, bo w konsoli zostanie zwrócony błąd
``` python
class Student:

    def __init__(self):
        self.__private_value = 7
        self.normal_value = 35
       
    def __private_function(self):
        ...
```
Uwaga! Do tak zdefiniowanych zmiennych/funkcji nadal możemy się dostać dodając na początku `_[nazwa_klasy]`, tj.
``` python
school = School() 
school._Student__private_value = 8
school._Student__private_function()
```

### Metody i pola
W Pythonie rozróżniamy:
- **metody i pola obiektu** - dotyczą bezpośrednio danego obiektu klasy/ mogą być wykonane na konktretnym obiekcie klasy
- **metody i pola klasy** - dotyczy całej klasy; zmienne klasy zapisujemy drukowanymi literami (traktujemy jako stałe), natomiast dla metod klasy przed ich definicją dajemy dekorator `@classmethod`

``` python
class ClassName:

    CLASS_VARIABLE = ...
    
    @classmethod   
    def class_function(cls, ...):
        ... cls.CLASS_VARIABLE ...
```
Do metod klasy odwołujemy się pisząc `ClassName.class_function()`, natomiast do pól klasy odwołujemy się na dwa sposoby (w zależności od miejsca) - albo przez klasę, tj. `cls.CLASS_VARIABLE` lub `ClassName.CLASS_VARIABLE`, albo przez już zdefiniowany obiekt klasy, tj. `self.CLASS_VARIABLE` lub `class_object.CLASS_VARIABLE`.

- **metody statyczne** - funkcje umieszczone wewnątrz klasy, które nie przyjmują argumentów `self` i `cls`; definijemy je zapisując przed nimi dekorator `@staticmethod`; wywołujemy ją za pomocą składni `ClassName.static_method()`; metody statyczne stosujemy jeżeli klasę chcemy potraktować jako pewien zbiór funkcji (podobnie możemy robić ze stałymi - grupować je w klasie )

### Funkcje jako obiekty
Funkcje możemy traktować jako obiekty i tym samym:
- tworzyć nowe funkcje przypisując do nich już istniejącą `new_function = original_function`
- podawać funkcje jako argumenty innych funkcji `def merged_func(first_func, second_func)`

*Zastosowanie:*
1. Często funkcji podaje się jako argumenty innych funkcji wtedy, kiedy chcemy **posortować obiekty**. Używamy wtedy funkcji `.sort(key=function)`, która działa w ten sposób, że dla każdego obiektu wyliczana jest wartość funkcji podanej jako `key`, a następnie wartości te są porównywane i sortowane.
2. Modyfikacja ogólnych algorytmów, czyli modyfikowanie jakiegoś działania.

### Lambda - funkcja anonimowa
Funkcja niepowiązana z żadną nazwą, wykorzystywana np. przy sortowaniu
``` python
objects_list.sort(key=lambda func_arguments: sort_func())
```

# PythON: Początek >> Niezbędzik adepta

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


# PythON: Początek >> Programowanie obiektowe - część 1
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
```__repr__ ```
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
`.sort()` - sortuje podaną listę i zastępuje ją

`.sorted()` - sortuje podaną listę i przypisuje ją do nowej listy

### Unpacking operators
przekazywanie operatorów pozycyjnych i nazwanych

- `*args` zbiera wszystkie przekazane argumenty pozycyjne, przy czym zmienna `args` jest typu *tuple*, czyli jest krotką
``` python
def calculate_sum_via_args(*args):
    ...

result_1 = calculate_sum_via_args(1, 2, 3, 4)
result_2 = calculate_sum_via_args(5, 6)
```
- `**kwargs` przekazywanie argumentów nazwanych, czyli słownikowych (typ *dict*)
``` python
def print_grades(**kwargs):
    ...
    
print_grades(
    matematyka = 3,
    fizyka = 5,
    chemia = 4
)
```

Unpacking operator `*` służy też rozpakowywaniu list:
``` python
numbers = [1, 2, 3, 4]

# error:
# result = calculate_sum_via_args(numbers)

#ok:
result = calculate_sum_via_args(*numbers)
```
co można użyć także przy łączeniu dwóch list
``` python
numbers_list_1 = [1, 2, 3, 4]
numbers_list_2 = [5, 6]
combined_numbers_list = [*numbers_list_1, *numbers_list_2]
```
Analogiczne działa operator `**` w konteście słowników.


# PythON: Początek >> Programowanie obiektowe - część 2

### Property jako getter i setter 

Zastosowanie **getter**:
- metoda, która zwraca wartość pola prywatnej z danej klasy; żeby ją zdefiniować używamy dekoratora `@property`, dzięki czemu możemy się do niego odnosić jak do pola klasy, ale nie możemy zmieniać wartości pola prywatnego; przyjmujemy, że getter nazywamy tak samo jak zmienną prywatną
``` python
class Student:
    def __init__(self):
        ...
        self._final_grades = []
        
    @property
    def final_grades(self):
        return self._final_grades
        
student = Sudent()
print(student.final_grades)
```

- wyciąganie wartości dynamicznych, liczonych za pomocą metod na podstawie pól klasy (skrócenie zapisu)

Zastosowanie **setter**:
- służy do ustawienia nowej wartości dla danego pola; jest to tzn. side effect, który służy modyfikacji pola przy przypisaniu nowej wartości
- walidacja poprawności ustawianej wartości; możemy zwalidować dodawane pole i w razie niespełnienia założeń zwrócić *exception*

``` python
class School:
    
    MAX_STUDENTS_NUMBER = 120
    
    def __init__(self, name, students):
        self._students = students
        self.departments = self._split_students_to_departments()
        ...
    
    @property
    def students(self):
        return self.students
        
    @students.setter
    def students(self, value):
        if len(value) < School.MAX_STUDENTS_NUMBER:
            self._students = value
        else:
            print("Przekroczono maksymalną liczbę uczniów")
            self._students = value[:School.MAX_STUDENTS_NUMBER]
        self.departments = self._split_students_to_departments()
    
```

### Dziedziczenie

W programowaniu możemy ustawić dziedziczenie między klasami definiując tym samym:
- *klasę bazową* (rodzica)
- *klasę potomną* (dziecko)

Dziecko dziedziczy wszystko od rodzica, ale może mieć zdefiniowane dodatkowe pola/metody, których nie ma rodzic.

W trakcie tworzenia konstruktora klasy potomenej musimy odwołać się do konstruktora klasy bazowej przy użyciu metody `super()`.
Powód: tworząc obiekt klasy potomnej (ze zmienionym konstruktorem) musimy użyć **obu konsturktorów**.
Jeżeli nie modyfikujemy konstruktora klasy potomnej, to domyślnie wywoływany jest konstruktor klasy bazowej.
``` python
#parent
class Teacher:
    
    def __init__(self, name, subject):
        self._name = name
        self._subject = subject
        self._assigned_departments = []
    ...
    #fields
    #methods
    
#child - identyczne jak rodzic
class English_Teacher(Teacher):
    pass
    
#child - rozszerzone
class Tutor(Teacher):

    def __init__(self, department, *args, **kwargs):
    #odwołanie się do konstruktora klasy basowej
    super().__init__(*args, **kwargs)
    #rozszerzenie klasy bazowej o dodatkowe pola
    self.guided_department = department
```

Metoda `super()` pozwala odwoływać się to wszystkich metod i pól klasy bazowej.

W klasach potomnych możemy nadpisać pola i metody z klasy bazowej 
definiując dane pole ponownie w konstruktorze (dopiero po wywołaniu konstruktora klasy bazowej!) lub definiując metodę o tej samej nazwie.

Uwaga: klasy mogą dziedziczyć także po typach wbudowanych, np. klasie `list`.

### Polimorfizm

Polimorfizm pozwala traktować obiekty, które są różnych klas (ale pochodzą od tej samej klasy bazowej) w ten sam sposób, 
tj. wykonujemy tę samą metodę (zdefiniowaną w klasie bazowej), ale mimo to jej działanie może być inne (nadpisane w klasach potomnych).


### Wielodziedziczenie i mixiny

**Wielodziedziczenie** - sytuacja, kiedy klasa dziedziczy po kilku klasach jednocześnie (w niektórych językach jest to niedozwolone).
Niebezpiecznym jest używanie wielodziedziczenia w kontekście stanu. Zasadne jest korzystanie z niego dla zachowania (metod).

Metoda `mro()` zastosowana na klasie potomnej pokazuje w jakiej kolejności Python będzie przeszukiwał klasy potomne pod kątem metod/pól

### Dobre praktyki w Pythonie
1. **Nie nadużywaj klas** - czasem lepiej jest zaimplementować plik z różnymi metodami zamiast robić klasę z funkcjami statycznymi
2. **Użyj property zamiast gettera/settera**
3. **Property getter i setter -> publiczne** - jeżeli getter i setter nie ma żadnej logiki, to najprawdopodobniej jest to pole publiczne, czyli zastosowanie gettera i settera jest zbędne.
4. **Nie nadużywaj property i side effect** - nie zawsze potrzebne są settery, czasem bezpieczniejsza jest implementacja metody
5. **Szanuj enkapsulację** - to, że pole jest publiczne nie znaczy, że możemy je dowolnie modyfikować
6. **Preferuj proste klasy zamiast słowników** - definiujemy je jako prostej klasy z konstruktorem i polami publicznymi
7. **Mixiny tylko do generycznych zastosowań**

#### SOLID
- **S = Single Responsibility Principle** (zasada pojedynczej odpowiedzialności) - każda klasa/moduł/funkcja/komponent
powinny mieć jedną i tylko jedną dobrze zdefiniowaną odpowiedzialność

- **O = Open/Close Principle Principle** (zasada otwarty/zamknięty) - powinniśmy tak konstruować klasy
by były one otwarte na rozszerzenie ale zamknięte na modyfikację

- **L = Liskov Substitution Principle** (zasada podstawienia Barbary Liskov) - klasa potomna 
powinna być szczególnym przypadkiem klasy bazowej

- **I = Interface Segregation Principle** (zasada segregacji interfejsów) - wiele bardziej wyspecjalizowanych interfejsów
jest lepsze niż jeden ogólny

- **D = Dependency Inversion Principle** (zasada odwórcenia zależności) - nasze klasy powinny
opierać się na abstrakcji, a nie szczegółach implementacji

#### DRY
**DRY = Don't Reapeat Yourself (nie powtarzaj się)** - poszczególne fragmenty logiki biznesowej nie powinny być wielokrotnie powielone

**Composition over inheritance** (kompozycja ponad dziedziczenie) - powinniśmy preferować tworzenie reużywalnych komponentów
wykorzystując kompozycję zamiast dziedziczenia

kompozycja - zawieranie instancji innych klas wewnątrz klasy

## Wbudowane struktury danych

#### Funkcje dotyczące typów `int` oraz `float`:
 
- `round(number)` - zaokrąglenie do najbliższej liczby parzystej
- `round(number, ndigits=x)` - zaokrąglenie do x miejsc po przecinku
- `floor(number)` - podłoga
- `ceil(number)` - sufit
- `int(number)` - rzutowanie, działa jak `floor()`
- `a ** b` lub `pow(a, b)` - potęgowanie; zwraca int/float
- `pow(a, b, mod=x)` - potęgowanie modulo x
- `math.pow(a, b)` - zawsze zwraca float
- `random.randint(a, b)` - losuje liczbę całkowitą (int) z przedziału (a,b)
- `random.uniform(a, b)` - losuje liczbę zmiennoprzecinkową (float) z przedziału (a,b)

#### Funkcje dotyczące typu `str`:

- `"connector_string".join(string_list)` - łączy napisy z listy `string_list`, 
rozdzielając poszczególne elementy napisem `connector_string`
- `.lstrip(chars_to_be_removed)`, `.lstrip(chars_to_be_removed)`, `.lstrip(chars_to_be_removed)` - 
usuwają poszczególne znaki (każdy rozważany osobno) `chars_to_be_removed` odpowiednio z lewej, prawej lub obu stron; jeśli nie podamy argumentu,
to funkcja domyślnie usunie białe znaki
- `.zfill(n)` - uzupełnia string tak, aby miał długość `n` i dopełnia go 0 (z przodu) do tej długości
- `.find(some_string)`, `.index(some_string)` - wskazuje pierwszy indeks, po którym występuje podany ciąg znaków;
w przypadku braku napisu, `.find()` zwraca -1, a `.index()` zwraca błąd
- `.find(some_string, starting_index)`, `.index(some_string, starting_index)` - wskazuje pierwszy indeks, 
po którym występuje podany ciąg znaków, ale zaczyna od indeksu `starting_index`
- 

#### Funkcje dotyczące typu `list`:

- `.clear()` - czyści listę
- `.reverse()` - odwraca kolejność elementów w liście
- `.count(element)` - liczy liczbę wystąpień `element` w liście
- `.copy()` - tworzy kopię listy
- `list_1.extend(list_2)` lub `list_1 += list_2` - do `list_1` dodaje `list_2`
- `.append(element)` - dodaje `element` do listy
- `list * n` - powiela n-razy wszystkie elementy w liście
- `list[n:m:k]` - zwraca co k-ty element z listy od n (włącznie) do m (wyłącznie)
- `list[:-m]` - zwraca elementy do elementu m (licząc od końca)


*List comprehensions* pozwalają na definiowanie list w bardziej skondensowany sposób, np.
- bez list comprehension
``` python
numbers = []
for number in range(15)
    if number % 2 == 0:
        numbers.append(number)
    else:
        numbers.append(-1)
```

- podstawowa składnia 
``` python 
numbers = [number for number in range(15)]
```

- składnia z opcjonalną częścią `if`
``` python 
numbers = [number for number in range(15) if number % 2 == 0]
```

Funkcja `enumetare(x)` zastosowana na krotce lub liście zwraca indeks elementu razem z tym elementem, tj.
``` python
fruits = ["banana", "apple", "berry"]
print(list(enumerate(fruits)))
# output: [(0, 'banana'), (1, 'apple'), (2, 'berry')]
```

- składnia z opcjonalną częścią `else`
``` python 
numbers = [number if number % 2 == 0 else -1 for number in range(15)]
```


#### Funkcje dotyczące typu `dict`:

- `.clear()` - czyści słownik
- `.copy()` - tworzy kopię słownika
- `.get(dict_key)` - wyciąga wartość słownikową znajdująca się pod `dict_key`, ale nie usuwa jej ze słownika;
działa podobnie jak `list[dict_key]`, ale w przypadku braku klucza zwraca `None`, a nie błąd
- `.get(dict_key, value)` - jeżeli klucz `dict_key` istnieje, to zwraca wartość słownikową, w p.p. `value`
- `.update(dict_key=value)` - aktualizuje słownik o nowy klucz `dict_key`;
jeśli klucz już istnieje, to zostaje nadpisany
- `.items()` - zwraca w formie listy pary elementów (klucz, wartość)

*Dict comprehensions* pozwalają na definiowanie słowników w bardziej skondensowany sposób, np.
- podstawowa składnia:
``` python
expenditures_names = ["prąd", "woda", "zakupy"]
expenditures = {expenditure_name: random.ranint(1, 100) for expenditure_name in expenditures_names}
```

- składnia rozszerzona o instrukcję warunkową if
``` python
students_names = ["Ola", "Marek", "Anna", "Konstanty"]
students = {random.randint(1,100): name for name in students_names if len(name) < 8}
```

- składnia rozszerzona o instrukcję warunkową if-else
``` python
students_names = ["Ola", "Marek", "Anna", "Konstanty"]
students = {
    random.randint(1,100): name if len(name) < 8 else f"{name[:5]}..."
    for name in students_names
}
```



*Set* to nieuporzadkowana kolekcja różnych (unikalnych) elementów. Nie możemy odwołać się do elementu zbioru
za pomocą indeksu. 

*Set* możemy zdefiniować bezpośrednio: 
``` python 
set_example = {element_1, element_2, ...}
```
lub korzystając z już zdefiniowanej listy:
``` python
set_example = set(list_example)
```

Pusty *set* inicjujemy jako `set()`.

#### Funkcje dotyczące typu `set`:

- `.add(element)` - dodaje element do setu
- `.remove(element)` - usuwa element z setu; jeżeli podanego elementu nie ma, to zostanie zwrócony błąd
- `.discard(element)` - usuwa element z setu; jeżeli podanego elementu nie ma, to nic się nie dzieje
- `.pop()` - wyciąga losowy element z setu i go usuwa
- `.copy()'` - kopiuje set
- `.clear()'` - czyści elementy ze zbioru
- `set_1.update(set_2)` - dodaje elementy z `set_2` do `set_1`
- `len(set)` - zwraca liczbę elementów w secie
- `set_1.union(set_2)` - tworzy sumę dwóch zbiorów
- `set_1.intersection(set_2)` - zwraca część wspólną zbiorów
- `set_1.difference(set_2)` - zwraca elementy zbioru `set_1`, których nie ma w `set_2`
- `set_1.issubset(set_2)` - sprawdza, czy `set_2` zawiera się w `set_1`

### Mutable i immutable
- **mutable** - jeżeli mamy kilka zmiennych wskazujących na ten sam obiekt, to jeżeli zmienimy jeden z nich, to zmienimy równocześnie wszystkie, np. *list, dict, set*, klasy własne
- **immutable** - jeżeli mamy kilka zmiennych zdefiniowanych o siebie, to po zmianie jednej, nie zmieni się druga, np. *str, int, float, str, bool, NoneType, tuple, frozenset, frozen dataclass*

`id(obiekt)` - zwraca adres danego obiektu w pamięci

**hashable** - oznacza, że obiekt ma hash value, które pozostaje niezmienione przez cały jego życie (mutable -> hashable)
- hashowalne obiekty mogą być kluczami w słowniku (*dict*)
- typy proste immutable są hashowalne
- kontenery mutable nie są hashowalne
- kontenery immutable (np. *tuple, frozenset*) są hashowalne jeżeli ich elementy są immutable
- klasy własne są domyślnie hashowalne
- mając własne `_eq_` w klasie mutable nie można implementować `_hash_`
- jeżeli klasa ma własne `_eq` a nie ma `_hash_`, to nie jest hashowalna

### Frozenset
- *set*, którego nie można modyfikować (nie ma metod, które służyłyby dodawaniu, usuwaniu lub modyfikacji elementów)
- można go tworzyć tylko przy wykorzystaniu konstruktora `frozenset`
- zawsze usuwa duplikaty
``` python
empty_frozenset = frozenset()
frozenset_from_set = frozenset(some_set)
frozenset_from_list = frozenset(some_list)
```
- pozwala na wykonywanie operacji matematycznych na zbiorach, tj. `union, intersection, difference, issubset`
- nie pozwanala na modyfikacje, a więc użycie takich metod jak np. `add, remove, discard, pop`

### Tuple (krotka)
- przechowuje elementy, do których możemy odwoływać się za pomocą konkretnych indeksów (jak lista)
- jest typem immutable (w przeciwieństwie do listy)
``` python
empty = tuple()
empty = ()
numbers = 1, 2
numbers = (1, 2)            #nawiasy zwiększają czytelność
numbers = tuple([1, 2])     #zamiana listy na krotkę
```
- w Pythonie nie istnieje tuple comprehensions

**Tuple - zastosowania:**
- argumenty z wykorzystaniem unpacking operators
- zwracając kilka wyników funkcji
``` python
def function_tuple():
    return value_1, value_2

#rozpakowywanie wyniku
assigned_value_1, assigned_value_2 = function_tuple()
```
- interacja z wykorzystaniem items albo enumerate
- jako kolekcja immutable
- grupując wartości różnych typów
- w specyficznych przypadkach ze względu na wydajność

### Named tuple
- pozwala odwoływać się do elementów krotki po nazwie
- definiujemy ją jako pewnego rodzaju szablon/klasę, który nazywamy PascalCasem
``` python
from collections import nametuple

Location = namedtuple("Location", ["latitude", "longitude"])

def run_example():
    location = Location(54.34, 16.64)
    print(location.latitude)
    print(location.longitude)
    
    # location = Location(latitude=54.34, longitude=16.64)
```
- `namedtuple` możemy traktować tak samo jak `tuple`, czyli odwoływać się do poszczególnych elementów korzystając z indeksów
- po `namedtuple` można również iterować
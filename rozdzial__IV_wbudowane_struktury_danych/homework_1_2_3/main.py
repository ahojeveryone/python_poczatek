import random
import math


def run_homework_1():

    float_list = []
    for _ in range(6):
        float_list.append(random.uniform(-20,20))
    print(float_list)

    int_list = []
    for _ in range(3):
        int_list.append(random.randint(1,10))
    print(int_list)


    modified_list = [round(float_list[0]), math.ceil(float_list[1]), math.floor(float_list[2])]
    for i in range(3):
       modified_list.append(pow(float_list[i+3], int_list[i]))
    print(modified_list)

def run_homework_2_ex1_ex4():

    first_name = input("Podaj imię: ").strip()
    last_name = input("Podaj nazwisko: ").strip()
    print(f"Nazywasz się {first_name} {last_name} - jak miło Cię poznać :)")
    print("Nazywasz się {} {} - jak miło Cię poznać :)".format(first_name, last_name))

def run_homework_2_ex2():

    identifier = str(random.randint(1, 99999)).zfill(5)
    print(f"Twoje wygenerowane id to: {identifier}")

def run_homework_2_ex3():

    favorite_colors = input("Podaj swoje ulubione kolory: ")

    # if favorite_colors.lower().find("niebieski") != -1:
    if "niebieski" in favorite_colors.lower():
        print("Jednym z twoich ulubionych kolorów jest niebieski.")
    else:
        print("Nie lubisz niebieskiego.")

def run_lesson_3():
    favourite_flavours = [
        "malinowy",
        "truskawkowy",
        "czekoladowy",
        "karmelowy"
    ]
    print(favourite_flavours)
    print(list(enumerate(favourite_flavours)))

def run_homework_3_ex1():
    numbers_divided_by_3 = [number for number in range(1, 31) if number % 3 == 0]
    numbers_divided_by_5 = [number for number in range(1, 31) if number % 5 == 0]
    # numbers_divided_by_3_or_5 = [*numbers_divided_by_3, *numbers_divided_by_5]
    numbers_divided_by_3_or_5 = numbers_divided_by_3 + numbers_divided_by_5
    print(numbers_divided_by_3)
    print(numbers_divided_by_5)
    print(numbers_divided_by_3_or_5)

def run_homework_3_ex2():
    sports_from_user = input("Please type in all your favourite sports. Each sport should be separated by a comma.")
    sports_list = [sport.strip() for sport in sports_from_user.split(',')]
    print(sports_list[1::2])

    chosen_sports_list = [sport for index, sport in enumerate(sports_list) if
                          index % 2 == 1]
    # print(sports_list)
    print(chosen_sports_list)


if __name__ == '__main__':
    run_homework_3_ex2()
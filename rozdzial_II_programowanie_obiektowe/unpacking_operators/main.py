import random

def create_string(*args):
    return "-".join(args)

    # result = ""
    # for word in args:
    #     result += str(word)
    #     result += "-"
    # return result[:-1]

def describe_dict(**kwargs):
    result = "describe_dict("
    for label, value in kwargs.items():
        if result != "describe_dict(":
            result += ", "
        result += f"{label}={value}"
    result += ")"
    print(result)

def generate_random_numbers():
    result = []
    for _ in range(random.randint(1,20)):
        result.append(random.randint(1,100))
    return result

if __name__ == "__main__":

    #ex_1
    print(create_string("ala", "ma", "kota", "3"))

    #ex_2
    describe_dict(
        first_name = "Mikołaj",
        age = 32
    )

    #ex_3
    whole_num_list_1 = generate_random_numbers()
    print(f"First list: {whole_num_list_1}")

    whole_num_list_2 = generate_random_numbers()
    print(f"Second list: {whole_num_list_2}")

    combined_list = [*whole_num_list_1, *whole_num_list_2]
    print(f"Combined list: {combined_list}")

    #ex_4
    first_dict = {
        "first_name": "Mikołaj",
        "age": 32
    }

    second_dict = {
        "second_name": "Olek",
        "sex": "male"
    }

    merged_dict = {**first_dict, **second_dict}
    print(merged_dict)
    describe_dict(**merged_dict)
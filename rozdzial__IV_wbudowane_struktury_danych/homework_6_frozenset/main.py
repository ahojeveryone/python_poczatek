import random


def create_frozenset_with_new_element(input_set=None):

    if input_set==None:
        input_set = frozenset()
    elif type(input_set)==set:
        input_set = frozenset(input_set)
    elif type(input_set)!=frozenset:
        print("Wrong argument!!!")
        return None

    output_set = input_set.union(({random.randint(0,10)}))
    #print(output_set)

    return output_set

def run_homework():

    input_set = set()
    all_sets = [input_set]
    while len(input_set)<11:
        input_set = create_frozenset_with_new_element(input_set)
        all_sets.append(input_set)

    print(all_sets)



if __name__ == '__main__':
    run_homework()

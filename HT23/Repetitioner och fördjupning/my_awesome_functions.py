import random

def remove_random_element(the_list : list):
    if isinstance(the_list, list):
        the_list.remove(random.choice(the_list))
    else:
        print("The parameter is not a list.")
import random


def random_numbers(size, avg):
    liste = random.sample(range(1, avg + 1), size)
    liste.sort()
    return ', '.join(str(a) for a in liste)


def exit_or_continue():
    key = input("Press \"Y\" to get new random number or \"N\" to exit: ")
    return key

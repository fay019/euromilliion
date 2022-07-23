import random


def random_numbers(size, avg):
    liste = random.sample(range(1, avg + 1), size)
    liste.sort()
    return liste

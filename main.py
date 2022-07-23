from my_random import random_numbers, exit_or_continue

first_time = True

while True:
    if first_time:
        print(f"Euro Million random \nnumber: {random_numbers(5, 50)} \nstars : {random_numbers(2, 12)}  ")
        first_time = False
    choice = exit_or_continue()
    if choice.lower() == "n":
        break
    elif choice.lower() == "y":
        first_time = True
    elif choice.lower() != "y":
        print("Only \"Y\" or \"N\" are valide")

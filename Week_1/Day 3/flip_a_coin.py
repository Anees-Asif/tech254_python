import random


def flip_a_coin():
    # Generate a random number
    number = random.randint(0, 1)

    if number == 0:
        return "Heads"
    else:
        return "Tails"


result = flip_a_coin()
print("The coins shows: ", result)

# Libraries and modules

# Python has very extensive libraries and modules

# Module = Single file of functions, classes, variables etc, that you can bring in and use in another python file

# Library = A collection of modules. Needs to be installed with pip.

import math
import random
import requests

num_float = 23.66

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)

rand_list = [1, 2, 3, 4, 5, 6, 7]
print(random.choice(rand_list))

ran_num = random.randint(1,10)
print(ran_num)


request_poke = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu/")
print(request_poke.status_code)
print(request_poke.content)


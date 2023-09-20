# Functions

# DRY - Don't Repeat Yourself

# Allow us to embed/reference code. making it reusable.

# Making a function

def print_something(print_string):
    print(print_string)


print_something("We can pass anything to the function")


def greeting(name):
    print(f"Helo, my name is {name}")


greeting("Anees")


# The return statement - holds a value and is used to pass data back to the print statement, so the output is printed

def addition(int1, int2):
    return int1 + int2


print(addition(2, 2))


# multiple arguments - used when you have a variable amount of items you want to pass. Must use "*" to define.

def multi_args(arg2, *multiargs):
    for arg in multiargs:
        print(arg)
    print(arg2)


multi_args(1, 2, 3, 4)

# Type hints - give IDE an idea of what type of data you expect the variables to be.

# Functions good practices

# Add useful comments to explain your functions
# Clear function names and argument names
# Keep your functions small and compact.
# Avoid duplication
# Correct indentation and formatting/syntax
# Organised properly
# Do not use them when not need
# Functions are start of your code
# Remember the return statement
# Consider using type hints

# Dictionaries in Python

In Python, dictionaries are used to store key-value pairs. The key is a reference to an object, and the value is the data storage mechanism you want to use.

```python
student_1 = {
    "name": "Anees",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["Variables", "Data Types", "Operators"]
}
print(student_1)

#Access Data using its keys
print(student_1["stream"])
print(student_1["completed_lesson_names"][0])


```
### Changing Values in a dictionary
```python
#Editing the value of the completed lessons key
student_1["completed_lessons"] = 3
#Printing the updated dict
print(student_1["completed_lessons"])

student_1["completed_lesson_names"].remove("Data Types")
print(student_1["completed_lesson_names"])
```
### Sets
```python
# Sets and frozen sets - there is no order

car_parts = {"wheels", "doors", "exhaust", "windows"}
print(car_parts)
car_parts.add("steering_wheel")
print(car_parts)
car_parts.discard("windows")
print(car_parts)
```

# Boolean Operations
Booleans are a data type representing truth values, with true and false being the two possible values

We have two Boolean variables `a` and `b`.

```python
a = True
b = False
print( a == b)
print ( a != b)
print( a >= b)
print(a <= b)
```
In the above code we are comparing the two variables, and are receiving outputs about whether they are true or false.
### String operations
We can also use operations on string to check if they satisfy a condition or not. In the first print, we are checking if "hi" contains orly alphabetical characters or not, and in this case it does so it will return true
```python
hi = "Hello World"
#Check if "hi" is any of the following
print(hi.isalpha())
print(hi.islower())
print(hi.endswith("!"))
```
# Data types + operators
Python is a dynamic language which means data types do not need to be specified, the interpreter will automatically assign the correct data type to the variable when it is declared.
```python
# Slicing a String - Begin from the 4th index
hw = "Hello world!"
print(hw[4:])

# Stripping Whitespace
strip_string = "Hi my name is Anees                               "
print(len(strip_string))
print((len(strip_string.strip())))

# Counting Substrings
example_text = "Here's some text with lot's of text"
print(example_text.count("text"))

# String Manipulation
print(example_text.lower())
print(example_text.capitalize())
print(example_text.replace("with", "without"))

# Casting and Arithmetic
a = 2
b = 5.4
c = "3"
print(a + b + int(c))

# F-Strings - Used to ignore the hassle of formating sentences
name = "Lassie"
years = "7"
height_cm = "60.2"
print(f"{name} is {years} years old and {height_cm} cm tall")

# Percentages -  Use :.0% to convert into a 0 decimal place percentage
score = 16
max_score = 26
print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:.2%}")
print(f"You scored {score/max_score:.0%}")
```
# List and Tuples
## Lists

Lists contains values at indexes, and items in the list can be accessed, removed or replaced. 

```python
shopping_list = ["Salad", "Eggs", "Doughnuts", "Milk", "Salmon"]

# Modify a list element
shopping_list[2] = "Tomato"

# List Methods
shopping_list.remove("Salad")
shopping_list.pop(2)
shopping_list.append("Carrots")
shopping_list.extend(["Water", "Celery"])

print(shopping_list)
```
### Mixed data type lists
We can also have different types of data within the same list
```python
mixture = [1, 2, 3.0, "one", "Two", "three"]

print(mixture)
print(mixture[1:3])
print(mixture[-2::])
#Will print the list backwards
print(mixture[::-1])
```
## Tuples
Tuples are immutable, which means they cannot be changed or edited.
```python
essentials = ("Bread", "Eggs", "Milk")
print(essentials)
```
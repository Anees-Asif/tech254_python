hw = "Hello word!"
print(hw[4:])

strip_string = "Hi my name is Anees                               "
print(len(strip_string))
print((len(strip_string.strip())))

example_text = "Here's some text with lot's of text"
print(example_text.count("text"))
print(example_text.lower())
print(example_text.capitalize())
print(example_text.replace("with", "without"))

#casting
a = 2
b = 5.4
c = "3"

print(a + b + int(c))

#Concatenation

d = "theres now a number 25.4 unless we put a space in"
print(str(a) + " ," + str(b) + d)

#f-strings
name = "Lassie"
years = "7"
height_cm = "60.2"

print(f"{name} is {years} years old and {height_cm} cm tall")

snoop = "Snoopy"
snoop_years = 52

print(f"{name.upper()} IS {snoop_years* 7} YEARS OLD IN DOG YEARS")

# Rounding
pi = 3.14159265359
print(f"Pi to 3 decimal places: {pi: .3f}")

#Percentages

score = 16
max_score = 26

print(f"You scored {score/max_score}")
print(f"You scored {score/max_score:.2%}")
print(f"You scored {score/max_score:.0%}")


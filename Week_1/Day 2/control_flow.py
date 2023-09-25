# Control Flow - Used to control the flow of your code, by making decisions
# Check if conditions are true before you run a piece of code. Can think of each control flow statement as a boolean.

# if

film_rating = "S"

if film_rating.lower() == "u":
    print("All age groups can watch this movie")

# elif - Less processing power and runs only if if condition is not met.

elif film_rating.lower() == "pg":
    print("Parental guidance is advised for this movie")
elif film_rating.lower() == "12" or film_rating.lower() == "12a":
    print("People aged 12 or over can watch this movie unsupervised. Younger people must be supervised.")
elif film_rating.lower() == "15":
    print("People aged 15 or over can watch this movie")
elif film_rating.lower() == "18":
    print("People aged 18 can watch this movie")

# else
else:
    print("This not a valid rating, please use 'u', 'pg','12' or '12a', '15', '18'")

# In Python there are no Switch statements or case statements. Python is nice and simple.

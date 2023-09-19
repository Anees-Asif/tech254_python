# Lists
shopping_list = ["Salad","Eggs", "Doughnuts", "Milk", "Salmon"]

# print(shopping_list)
# print(shopping_list[0])
shopping_list[2] = "Tomato"


#list methods
shopping_list.remove("Salad")
shopping_list.pop(2)

shopping_list.append("Carrots")

shopping_list.extend(["Water", "Celery"])
print(shopping_list)

# Mixed data types list

mixture = [1,2,3.0, "one","Two","three"]
print(mixture)

print(mixture[1:3])
print((mixture[-2::]))
print((mixture[::-1]))

#tuples
essentials = ("Bread", "eggs", "milk")
print (essentials)


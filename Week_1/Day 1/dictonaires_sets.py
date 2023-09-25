#key is reference tp object
#value is the data storage mechanism you want to use

student_1 = {
    "name": "Anees",
    "stream": "DevOps",
    "completed_lessons": 4,
    "completed_lesson_names": ["Variables", "Data Types", "Operators"]
}
print(student_1)

#Acesing data using keys

print(student_1["stream"])
print(student_1["completed_lesson_names"][0])

#changing a value in a dict

student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])

student_1["completed_lesson_names"].remove("Data Types")
print(student_1["completed_lesson_names"])

#Gettin the keys

print(student_1.keys())

# Sets and frozen sets - there is no order

car_parts = {"wheels", "doors", "exhaust", "windows"}
print(car_parts)
car_parts.add("steering_wheel")
print(car_parts)
car_parts.discard("windows")
print(car_parts)
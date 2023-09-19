
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print(f"Your bmi is: {bmi:.1f}")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("Your weight is normal.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")

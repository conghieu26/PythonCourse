# Python weight converter

weight = float(input("Please enter your weight: "))
unit = input("Kilogram or Pound? (k or L): ")

if unit == "l":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "k":
    weight = weight / 2.205
    unit = "kg"
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not a valid unit")




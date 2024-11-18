#Write a Python program that asks the user for the radius of a circle 
#Then calculates and prints the area of the circle.
try:
    r = float(input("Enter radius of circle: "))
    if r <= 0:
        raise ValueError("Radius can only be a positive number.")
    else:
        print("Area of circle is =", 3.14 * r * r)

except ValueError as ve:
    print(ve)
except Exception as e:
    print("Invalid Input")

    
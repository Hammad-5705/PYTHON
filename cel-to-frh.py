#Write a program that converts a temperature in Celsius to Fahrenheit.
try:
    c=float(input("Enter Celsius= "))
    f=(9/5)*c+32
    print(f)
except ValueError:
    print("Invalid input")

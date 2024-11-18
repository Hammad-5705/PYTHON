#Write a program that asks the user for the length and width of a rectangle 
#Then calculates and prints the area of the rectangle.

try:
    l=float(input("Enter Length of rectangle"))
    w=float(input("Enter Width of rectangle"))

    if w<=0 or l<=0:
        raise ValueError("values must be positive")
    else:
        a=l*w
        print("Area = " ,a )

except ValueError as ve:
    print(ve)

except Exception as e:
    print(e)
#Write a Python program that asks the user to enter an integer
#Then determines and prints whether the entered number is even or odd.

try:
    n=float(input("Enter number"))
    if(n%2!=0):
        print("Odd")
    else:
        print("Even")
except ValueError:
    print("Invalid Input")
#Write a Python program that takes an integer as input from the user and calculates the sum of its digits.

try:
    n=int(input("Enter the Number= "))
    if n<=9:
        raise ValueError("Enter Numbers greater than 9")
    else:
        s=0
        while n>0:
            m=n%10
            n=n//10
            s=s+m
        print("sum of digits= ",s)
except ValueError as ve:
    print(ve)
except Exception as e:
    print("Invalid input")
#Write a Python program that takes a string as input from the user and prints the reverse of that string.

s=input("Enter string")
#  using reversed function with join
#rs=''.join(reversed(s))

#using slicing method
try:
    rs=s[::-1]
    if not s:
        raise ValueError("String shouldnt be empty")
    else:
        print(rs)

        
except ValueError as ve:
    print(ve)

except Exception as e:
    print("Invalid Input")


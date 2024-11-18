def fx():
    raise ValueError("Invalid Input")


a=input("Enter Number betwen 1 and 5 : ")

if not a=="quit":
    try:
         num=int(a)
         print("Valid Input")
    except:
        fx()
else:
    print("quit")



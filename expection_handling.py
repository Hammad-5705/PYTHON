try:
    a=[]
    a=int(input("Enter Number in list"))
    print(a)
# except Exception as e:
#     print(e)
except ValueError:
    print("Value Error")
except IndexError:
    print("Value Error")

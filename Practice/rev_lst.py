def inp():
    try:
        lst=int(input("Enter Numbers"))
        rev(str(lst))

    except Exception as e:
        print(e)

def rev(lst):
    lst=lst[::-1]
    pnt(lst)

def pnt(lst):
    print(f"The Reversed string is {lst}")

inp()
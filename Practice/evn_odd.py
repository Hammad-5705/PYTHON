def chk(num):
    
    if(num%2==0):
        pevn(num)
            
    else:
        podd(num)
        



    

def pevn(num):
    print(f"{num} is Even")


def podd(num):
    print(f"{num} is Odd")


def inp():
    try:
        num=int(input("Enter Number to check :"))
        chk(num)

    except ValueError:
        print("Value Error")
        return 0


num=inp()

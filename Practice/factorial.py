def inp():

    try:
        num=int(input("Enter Number to find factorial : "))
        y=calc(num)
        pfac(num,y)
    
    except ValueError:
        print("Invalid Input")

    
def calc(num):

    if num==1 or num==0:
        return(1)
        

    
    else:
        return num*calc(num-1)
        

def pfac(num,fac):
    print(f"factorial of {num} is {fac}")


inp()

    
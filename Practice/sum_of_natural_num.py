def inp():
    try:
        s=int(input("Enter Starting point: "))
        s=ntrl(s)
        
        e=int(input("enter ending point: "))
        if e<=s:
            raise ValueError

        sum=calc(s,e)

        pnt(s,e,sum)

        

    except ValueError:
        print("Invalid Input")


def ntrl(s):
    if s>0:
        return s
        
    
    else:
        err()


def err():
    raise ValueError


def calc(s,e):
    i=s
    sum=0
    while(i<=e):
        sum=s+sum
        s+=1
        i+=1

    return(sum)


def pnt(s,e,sum):
    print(f"The sum of Nabutal numbers between {s} and {e} is {sum}")


inp()
square = lambda num: num**2

print(square(7))



def avg(sum , den):
    a=int(input("Enter number"))
    b=int(input("Enter number"))
    c=int(input("Enter number"))
    return (sum(a,b,c)/den)
    


print(avg(lambda a,b,c: a+b+c , 3))
# def fx(a,b):
#     if(a>b):
#         print(a," is greater than ",b)
#     else:
#         print(b," is greater than ",a)

# x=int(input("Enter first num : "))
# y=int(input("Enter second number : "))
# fx(x,y)





# def fx(*a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     return sum

# values = input("Enter values separated by spaces: ").split()
# values = [int(value) for value in values] 

# answer=fx(*values)
# print(answer)



def fx2(*x):
    mul=1
    lan=len(x)
    for i in x:
        mul=mul*i
    print(mul,lan)
    gm(mul,lan)


def gm(ml,ln):
    GM=ml**(1/ln) 
    dsp(GM)

def dsp(pr):
    print("Geometric mean =: ",pr)

if __name__=="__main__":
    print("seprate each value by space".title())
    values=input("Enter Values of X: ").split()
    values=[int(X) for X in values]

    print(values,"\n\n\n\n")

    fx2(*values)





# def aveage(*avg):
#     sum=0
#     for i in avg:
#         sum=sum+i
#     average=sum/len(avg)
#     print(sum)
#     print(len(avg))
#     print("Average = " , average)

# aveage(1,2,3,4)








































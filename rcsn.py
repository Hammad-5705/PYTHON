# def fac(n):

#     if n==0 or n==1:
#         return 1
    
#     else:
#         return (n*fac(n-1))
    
# print(fac(int(input("Enter number you want to get factorial:  "))))


def fabonaci_series(n):

    if n==0:
        return 0
    
    elif n==1:
        return 1
    
    else:
        return (fabonaci_series(n-1)+fabonaci_series(n-2))
    
print(fabonaci_series(float(input("Enter Number You Want To Get Fabonaci series: "))))

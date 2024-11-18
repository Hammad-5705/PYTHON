def fx(num):
    '''This is a doc string it defines the function'''
    print(num**2)

n=int(input("Enter number to get square"))
fx(n)
print(fx.__doc__)

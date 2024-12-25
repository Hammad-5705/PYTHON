# Write a generator function called fibonacci() that generates an infinite sequence of Fibonacci numbers. 
# The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.
# Your generator should yield Fibonacci numbers indefinitely, allowing the caller to request as many values as needed. 
# Also, demonstrate how to use this generator to print the first 10 Fibonacci numbers.

def fab(num):
    ser=[]
    if num==0:
        return (ser.append(0))

    elif num==1:
        for i in range(2):
            return (ser.append(1))
            

    else:
        ser.append(0)
        ser.append(1)
        for i in range(2,num+1):
            ser.append(ser[-1]+ser[-2])
        return ser

def generator(n):
    res=fab(n)
    for i in res:
        yield i

n=input("number to get fabinacci series: ")
gen=generator(int(n))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))



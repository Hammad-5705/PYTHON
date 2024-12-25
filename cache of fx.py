# You need to implement a function that calculates the factorial of a given non-negative integer n. 
# The factorial function is defined as:

# factorial(0) = 1
# factorial(n) = n * factorial(n - 1) for n > 0
    
# Given that calculating factorials can be computationally expensive for large n, 
# you should use the functools.lru_cache decorator to cache the results of the factorial function to improve performance.

import functools
import time

@functools.lru_cache(maxsize=None)
def factorial(num):
    time.sleep(10)
    result=1
    if num==0:
        return 0
    else:
        for i in range(1,num):
            result=result*i
        return result

while True:
    num=int(input("Enter number to calculate factorial"))
    if num>=0:
        res=factorial(num)
        print(res)

    else:
        break



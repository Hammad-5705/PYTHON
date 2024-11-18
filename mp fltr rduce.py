l=[ x for x in range(100+1) if x>0]

ll=list(map(lambda x:x**2 , l))
print( f"\nThe Square of list is {ll}")

lll=list(filter(lambda x: x<=100 , ll))
print(f"The Squares that are greater less than 101 are \n {lll}")

from functools import reduce
llll=reduce(lambda x,y: x+y , ll)
print(f"The sum of whole list is {llll}")
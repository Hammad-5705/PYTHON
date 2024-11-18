s3={1,3,5,7,9,10}
s2={2,4,6,8,10}
s1={1,3,5,7,9}

print(s1.union(s2))

print(s1)
s4=s1.update(s2)
print(s4)

print(s1,"\n\n",s2)

print(s3.intersection(s2))

print("\n\n",s3,"\n",s2)
# s3.intersection_update(s2)
# print(s3)


print(s3.symmetric_difference(s2))
# s3.symmetric_difference_update(s2)

u={0,1,2,3,4,5,6,7,8,9,10}
print(u,s3)
print(s3.isdisjoint(u))     #check if s3 not having even a single value of U
print(s3.issuperset(u))     #check if U having values of s3
print(s3.issubset(u))       # check if all values of s3 equals to u 

print(u.isdisjoint(s3))
print(u.issuperset(s3))
print(u.issubset(s3))

print(u)

u.add(11)
print(u)

# u.remove(19)
# print(u)

u.discard(11)
print(u)

# del s1,s2,s3,s4
# print(s1,s2,s3,s4)


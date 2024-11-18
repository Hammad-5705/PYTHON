
# a=[3,4,5,6,7,8,9,10,"Hello",True]
# print(a)
# i=0
# while(i<len(a)):
#     print(a[i])
#     i+=1

a=[x for x in range(101) if x%2==0]
i=0
while (i<len(a)):
    print(a[i])
    i+=1
print(a)
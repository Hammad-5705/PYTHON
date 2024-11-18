# with open('tst.txt','r') as f:
#     while True:
#         txt=f.readline()
#         print(txt)
#         if not txt:
#             break


with open('tst.txt','r') as f:
    i=0
    while True:
        marks=f.readline()
        i=i+1

        if not marks:
            break
    
        m1=int(marks.split(" ")[0])
        m2=int(marks.split(" ")[1])
        m3=int(marks.split(" ")[2])
        m4=int(marks.split(" ")[3])

        print(f"The marks of student {i} in english is {m1}")
        print(f"The marks of student {i} in urdu is {m2}")
        print(f"The marks of student {i} in math is {m3}")
        print(f"The marks of student {i} in computer is {m4}")
        print("")










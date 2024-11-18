# with open('tst.txt','r') as f:
#     f.seek(10)
#     print(f.tell())
#     txt=f.read(2)
#     print(txt)

with open('tst.txt','w') as f:
    inp=input("Enter text to write in file : ")
    txt=f.write(inp)
    f.truncate(5)

with open('tst.txt','r') as f:
    print(f.read())
    
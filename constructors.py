class student:

    def __init__(self,n,fn,c,r,ad) -> None:
        self.name=n
        self.father_name=fn
        self.clas=c
        self.rolno=r
        self.address=ad

    def __str__(self):
        return (f"\n\n\nStudent name : {self.name} \nFather Name : {self.father_name}"
                f"\nClass : {self.clas} \nRolno : {self.rolno} \nAddress : {self.address}")





def inp():
    name=input("Enter Name of Student : ")
    fname=input("Enter Father Name of Student : ")
    clas=input("Enter Class of Student : ")
    rolno=input("Enter Rolno of Student : ")
    adress=input("Enter Address of Student : ")
    return str(student(name,fname,clas,rolno,fname))




def write():
    with open("student Constructor.txt","w+") as f:
        v=str(inp())
        txt=f.write(v)


def read():
    with open("student Constructor.txt","r+") as f:
        txt=f.read()
        print(txt)


def choise():
    i=input("Press R to read File and W to write in file : ")

    if i.lower()=='w':
        write()

    elif i.lower()=='r':
        read()

    else:
        raise ValueError



        

i=1
while (i==1):
    a=input("\n\n\nPress 1 to continue or Press any key to Stop : ")
    if a=='1':
        choise()
         
    else:
        break

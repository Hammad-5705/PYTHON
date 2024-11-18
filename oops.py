class student:
    name="ABC"
    clas="7"
    rolno="232"
    fname="Abc"
    adress="ABC"

    def __str__(self):
       return (f"\n\n\nStudent name : {self.name} \nFather Name : {self.fname}"
            f"\nClass : {self.clas} \nRolno : {self.rolno} \nAddress : {self.adress}")
   
    def inp(self):
        self.name=input("Enter Name of Student : ")
        self.fname=input("Enter Father Name of Student : ")
        self.clas=input("Enter Class of Student : ")
        self.rolno=input("Enter Rolno of Student : ")
        self.adress=input("Enter Address of Student : ")



def write():
    with open("student.txt","w+") as f:
        s=student()
        s.inp()
        txt=f.write(str(s))


def read():
    with open("student.txt","r+") as f:
        txt=f.read()
        print(txt)

def choise():
    i=input("Press R to read File and W to write in file")

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

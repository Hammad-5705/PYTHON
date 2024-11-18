# Define an Employee class with private attributes _name and _salary. 
# Use property decorators to get the name and salary. 
# Ensure the salary is a positive number in the setter.

class emp:

    def __init__(self) -> None:
        self._name=0
        self._salary=0
        

    @property
    def name(self):
        return self._name
    
    @property
    def salary(self):
        return self._salary
    
    @name.setter
    def name(self,n):
        self._name=n

    @salary.setter
    def salary(self,s):

        if int(s)>0:
            self._salary=s

        else:
            raise ValueError("\n\n\nSalary should be greater than 0 ")
        
    def __str__(self) -> str:
        return f"{self._name} {self._salary}"
        
a=emp()
a.name="Hammad"
a.salary="20000"

b=emp()
b.name="Zeeshan"
b.salary=23000

print(a)
print(b)

    
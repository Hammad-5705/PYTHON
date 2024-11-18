# Person Class: Create a Person class with a private attribute _age. 
# Implement a getter and setter for _age. 
# Ensure the age cannot be set to a negative number using the setter.

class person:
    def __init__(self) -> None:
        self._age=0

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,a):
            
            if(a>0):
                self._age=a

            else:
                 raise ValueError("Age cant be 0 or negative.")


c=person()
c.age=int(input("Enter Your age : "))







class std:
    def __init__(self) -> None:
        self.__name=0

    # @property
    # def name(self):
    #     return self.__name
    
    # @name.setter
    # def name(self,n):
    #     self.__name=n

    # def __str__(self) -> str:
    #     return f"{self.__name}"

s=std()
s._std__name="Ali"
print(s._std__name)

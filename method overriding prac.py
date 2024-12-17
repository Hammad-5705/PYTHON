class account:
    def __init__(self,num,name) -> None:
        self._num=str(num)
        self._name=str(name)
        self._bal=float(0)


    @property
    def balance(self):
        return self._bal
    @balance.setter
    def number(self,b):
        self._bal=b

    def deposit(self,a):
        self._bal=self._bal+a
        return print(self._bal,"has been deposited")
    
    def withdraw(self,a):
        self._bal=self._bal-a
        return print(f"{a} has been Withdraw remaning amount is {self._bal}")
        

class saving_account(account):
    check=0

    def __init_subclass__(cls) -> None:
        cls.check=cls.check+1
        return super().__init_subclass__()   
    
    def withdraw(self, a):

        if self.check<10:
            return super().withdraw(a)
        else:
            return print((f"No more withdraw can be made for this month").title())
        
class cheking_account(saving_account):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()
    
    def withdraw(self, a):
        if self._bal<-5000:
            return print((f"Over Draft limit has been reached").title())
        else:
           return super().withdraw(a)
        
# a=account("SKTICSSM1905705","Taha")
# a.deposit(5000)
# a.withdraw(30)

# s=saving_account("SKTICSSM1905705","Taha")
# s.deposit(50)
# for i in range(10):
#     s.withdraw(70)
# s.withdraw(70)

c=cheking_account("SKTICSSM1905705","Taha")
c.deposit(70)
c.withdraw(5000)


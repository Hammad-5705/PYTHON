class calc:
    def __init__(self) -> None:
        self._num=[]

    @property
    def num(self):
        return self._num
    
    @num.setter
    def num(self,n):
        self._num=n

    @staticmethod
    def add(a):
        return a[0]+a[1]
    
c=calc()
c.num=[3,5]
print(c.add(c.num))
class father:
    def __init__(self) -> None:
        self._fn=0

    @property
    def fn(self):
        return self._fn
    
    @fn.setter
    def fn(self,n):
        self._fn=n

class mother:
    def __init__(self) -> None:
        self._mn=0

    @property
    def mn(self):
        return self._mn
    
    @mn.setter
    def mn(self,m):
        self._mn=m

class child(father,mother):
    def __init__(self) -> None:
        super().__init__()
        self._cn=0

    @property
    def cn(self):
        return self._cn
    
    @cn.setter
    def cn(self,n):
        self._cn=n

    def __str__(self) -> str:
        return f"{self._fn} {self._mn} {self._cn}"


C=child()
C.fn="Jerry"
C.mn="Rom"
C.cn="Alpino"
print(C)
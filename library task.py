class library:

    def __init__(self) -> None:
        self._nb=0
        self._books=[]

    @property 
    def nb(self):
        return self._nb
    
    @nb.setter
    def nb(self,n):
        self._nb=n

    @property 
    def books(self):
        return self._books
    
    @books.setter
    def books(self,b):
        self._books=b

    def check(self):
        if self._nb==len(self._books):
            print("Equal Quantity")

        else:
            print("Not Equal Quantity")

    
l=library()
B=["jannat k patay","Pir e kamil"]
l.books=B
l.nb=2
l.check()

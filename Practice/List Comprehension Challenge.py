try:
    def fx(x):
        c=0
        for i in range(2,x):
            if x%i==0:
                c=c+1

        if c>0:
           return c
        
        else:
            return 0

            
                    
    def calc():
        lst=[x for x in range(1,1000+1) if fx(x)==0]
        pnt(lst)

    def pnt(lst):
        print(f"The prime numbers between 1 to 1000 are as follow")
        for i in lst:
            print(i)

except:
    raise SyntaxError


calc()
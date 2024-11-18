try:
    def inp():
        num=int(input("Enter +ve Number to find factorial"))
        cnfrm(num)
        calc(num)

    def cnfrm(num):
        if num>0:
            return 0
        
        if num <0 or num==0:
            raise ValueError
        
    def calc(num):

        # fac=1
        # inum=num
        # while(inum>=1):
        #  fac=fac*inum
        #  inum=inum-1

        fac=1
        for i in range(1,num+1):
         fac=fac*i


        pnt(num,fac)


    def pnt(num,fac):
        print(f"The Factorial of {num} is {fac}")


    inp()



except:
    raise ValueError
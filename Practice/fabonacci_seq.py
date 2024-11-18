try:
    def inp():
        num=int(input("Enter Number to calculate fabonacci: "))
        num=chk(num)
        fab(num)

except:
    raise ValueError


def chk(num):
    if num<0:
        raise ValueError
    else:
        return(num)
    

def fab(num):
    global ser
    if num==0:
        ser.append(0)

    elif num==1:
        ser.extend([0,1])

    else:
        ser.extend([0,1])
        for i in range(2,num):
            ser.append(ser[-1]+ser[-2])

    


       
    pnt(ser)    
        

def pnt(ser):
    print(ser)

    
ser=[]
inp()
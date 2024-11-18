def inp():
    print("Welcome to Multiply Matrix")
    call()

def matrix_A():
    print("CHoose order of Matrix")
    r=int(input("Enter Number of Rows : "))
    c=int(input("Enter number of Coloms : "))

    if r==1 and c==1:
        arow=[]
        arow.extend(inp_one())
        return arow

    elif r==2 and c==2:
        arow=[]
        arow.extend(inp_two())
        return arow

    elif r==3 and c==3:
        arow=[]
        arow.extend(inp_three())
        return arow
    
    else:
        raise ValueError

def matrix_B():
    print("CHoose order of Matrix")
    r=int(input("Enter Number of Rows : "))
    c=int(input("Enter number of Coloms : "))

    if r==1 and c==1:
        brow=[]
        brow.extend(inp_one())
        return brow

    elif r==2 and c==2:
        brow=[]
        brow.extend(inp_two())
        return brow


    elif r==3 and c==3:
        brow=[]
        brow.extend(inp_three())
        return brow
    
    else:
        print("Enter square matrix of order 1x1 2x2 or 3x3 ")






def inp_one():
    r=[]
    r.append(int(input("Enter row Value 1: ")))
    m=[]
    m=r
    return m



def inp_two():
    c1=[]
    c2=[]
    c1.append(int(input("Enter row 1 col 1 : ")))
    c1.append(int(input("Enter row 1 colomn 2: ")))
    c2.append(int(input("Enter row 2 colomn 1: ")))
    c2.append(int(input("Enter row 2 colomn 2: ")))
    m=[c1,c2]
    return m



def inp_three():
    c1=[]
    c2=[]
    c3=[]
    c1.append(int(input("Enter row 1 col 1 : ")))
    c1.append(int(input("Enter row 1 colomn 2: ")))
    c1.append(int(input("Enter row 1 colomn 3: ")))

    c2.append(int(input("Enter row 2 colomn 1: ")))
    c2.append(int(input("Enter row 2 col 2 : ")))
    c2.append(int(input("Enter row 2 colomn 3: ")))

    c3.append(int(input("Enter row 3 colomn 1: ")))
    c3.append(int(input("Enter row 3 colomn 2: ")))
    c3.append(int(input("Enter row 3 col 3 : ")))

    m=[]
    m=[c1,c2,c3]
    return m


def call():
    print("Enter Matrix A ")
    A=matrix_A()
    print("Enter Matrix B ")
    B=matrix_B()

    if len(A)==len(B):
        calc(A,B)

    else:
        print("Order of matrix arent match")
        raise ValueError
    

def calc(A,B):

    if len(A)==1 and len(B)==1:
        ans=A[0]*B[0]
        print(f" {A} X {B}\n={ans}")
    
    elif len(A)==2 and len(B)==2:

        y1=A[0]
        y2=A[1]

        z1=B[0]
        z2=B[1]
        
        ans=[
            ( (y1[0]*z1[0]) + (y1[1]*z2[0]) )   , ( (y1[0]*z1[1]) + (y1[1]*z2[1]) ) ,
            ( (y2[0]*z1[0]) + (y2[1]*z2[0]) ) , ( (y2[0]*z1[1]) + (y2[1]*z2[1]) ) 
         ]
        
        print(f" {y1}   {z1}\n {y2} X {z2}\n\n={ans[0]} {ans[1]}\n {ans[2]} {ans[3]}")
    
    elif len(A)==3 and len(B)==3:

        y0=A[0]
        y1=A[1]
        y2=A[2]

        z0=B[0]
        z1=B[1]
        z2=B[2]

        ans=[ 
            ( (y0[0]*z0[0])+(y0[1]*z1[0])+(y0[2]*z2[0])) , ( (y0[0]*z0[1])+(y0[1]*z1[1])+(y0[2]*z2[1])) , ((y0[0]*z0[2])+(y0[1]*z1[2])+(y0[2]*z2[2])) ,
            ( (y1[0]*z0[0])+(y1[1]*z1[0])+(y1[2]*z2[0])) , ( (y1[0]*z0[1])+(y1[1]*z1[1])+(y1[2]*z2[1])) , ((y1[0]*z0[2])+(y1[1]*z1[2])+(y1[2]*z2[2])) ,
            ( (y2[0]*z0[0])+(y2[1]*z1[0])+(y2[2]*z2[0])) , ( (y2[0]*z0[1])+(y2[1]*z1[1])+(y2[2]*z2[1])) , ((y2[0]*z0[2])+(y2[1]*z1[2])+(y2[2]*z2[2]))          
        ]
        print(f"{y0}   {z0}\n {y1} X {z1}   {y2}   {z2}\n\n={ans[0]} {ans[1]} {ans[2]} \n {ans[3]} {ans[4]} {ans[5]}\n {ans[6]} {ans[7]} {ans[8]}")
        
    
inp()
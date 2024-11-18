try:
    def inp():
     num=int(input("Enter a Number"))
     chk(num)

except Exception as e:
      print(e)

def chk(num):

    a=2
    while(a<num):
        if(num%a==0):
            pnterr(num)
            break

        else:
            pnt(num)
            break

        a+=1

def pnt(num):
    print(f"The number {num} is Prime")

def pnterr(num):
    print(f"The number {num} isn't prime")
    

inp()
a=1

while(a<=100):

    if(a%2==0):
        print("Continue",a)
        a+=1
        continue
        

    elif(a*10==110):
        print("Break",a)
        break
        

    else:
        print(a)
        a+=1
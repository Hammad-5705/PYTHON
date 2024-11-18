import datetime

x=datetime.datetime.now()

hrs=x.strftime("%H")
mins=x.strftime("%M")
secs=x.strftime("%S")
a=int(x.strftime("%M"))
print(type(a))

print("Current Time Is: ",hrs," :",mins, " :", secs)

if(int(hrs)<12):
    if(int(mins)>0):
        msg="good morning sir"
        print(msg.title())
    

elif((int(hrs)>=12) and (int(hrs)<6)):
    msg="good afternoon sir"
    print(msg.title())
    

elif(int(hrs)>=6):
    msg="good Night sir"
    print(msg.title())

else:
    print("Invalid Time")


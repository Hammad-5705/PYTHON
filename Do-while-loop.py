# python doesnt support do while loop so that we have to make our own

a=int(input("Enter Value of a : "))

while True:
    print("Itration no: ",a)
    a+=1

    if(a>10):
        print("The End")
        break
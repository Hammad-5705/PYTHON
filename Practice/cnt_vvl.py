try:
    def inp():
        a=input("Enter a String ")
        calc(a)

except Exception as e:
    print(e)

def calc(a):

    vowels=0
    a.lower()
    for i in a:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
            vowels+=1
    
    pnt(a,vowels)

def pnt(a,vowels):
    print(f"The string \"{a}\" has {vowels} vowels")


inp()
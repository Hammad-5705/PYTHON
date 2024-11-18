# Caesar Cipher
# Write a program to implement the Caesar Cipher encryption. Take a string and shift each letter by a specified number of places.

def choice():
    chs=int(input("Press 1 to encrypt and 2 to decrypt a message"))

    if chs==1:
        print(enc())

    elif chs==2:
        print(dec())

    else:
        raise ValueError
    
def fx(st):
    return list(st.lower())
        
def enc():
    st=input("Enter String to encrypt message: ")
    a=fx(st)
   
    ii=0

    for i in range(len(a)):
        

        if a[ii]=='a':
            a[ii]='x'

        elif a[ii]=='b':
            a[ii]='y'

        elif a[ii]=='c':
            a[ii]='z'

        elif a[ii]==" ":
            a[ii]=a[ii]

        elif 'a'<=a[ii] or a[ii]<='z':
            a[ii]=chr(ord(a[ii])-3)


        ii+=1
    return "".join(a)


def dec():
    st=input("Enter String to Decrypt message: ")
    a=fx(st)
   
    ii=0

    for i in range(len(a)):
        

        if a[ii]=='x':
            a[ii]='a'

        elif a[ii]=='y':
            a[ii]='b'

        elif a[ii]=='z':
            a[ii]='c'

        elif a[ii]==" ":
            a[ii]==a[ii]

        elif 'a'<=a[ii] or a[ii]<='z':
            a[ii]=chr(ord(a[ii])+3)

        ii+=1
    return "".join(a)    





        
choice()
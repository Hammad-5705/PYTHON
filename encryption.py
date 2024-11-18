# Write a python program to translate a message into secret code language. 
# Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end 
# now append three random characters at the starting and the end else: simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it 
# else: remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode


def E_prnt(text):
    txt=enc(text.split(" "))

    txxt=""
    for q in range(len(txt)):
        txxt=f"{txxt} {txt[q]}"

    print(txxt)
    return 0


def rs(text):
    result = ""
    for char in text:
        result = char + result
    return result

def enc(msg):
    
    
    fnl=[]

    for i in range(len(msg)):
        lst=msg[i]
        

        if(len(lst)>=3):

           
            
            lst+=lst[0]
                
            
            lst=lst[1:]
            nlst=lst

            for x in range(3):
                nlst=f"{nlst[x-len(lst)]}{nlst}"

                
            for xx in range(3):
                nlst=f"{nlst}{nlst[xx+len(lst)%3]}"
            
            fnl.append(nlst)

        else:
            fnl.append(rs(lst))
            
    return fnl
        
def ask():
    aask=input("Enter E to Encrypt and D to Decrypt Message : ")

    if(aask.lower()=='e'):
        enter_msg_E()
    
    elif(aask.lower()=='d'):
        enter_msg_D()
    
    else:
        raise ValueError("Invalid Input")
    



def enter_msg_E():
    s=input("Write your message to Encrypt : ")
    E_prnt(s)
    return 0


def enter_msg_D():
    s=input("Write your message to Decrypt : ")
    D_prnt(s)
    return 0


def dec(m):
    fnl=[]

    for i in range(len(m)):
        lst=m[i]

        if (len(lst)<3):
            fnl.append(rs(lst))
        
        else:
            lst=lst[3:-3]
            lst = lst[-1:] + lst[:-1]            
            fnl.append(lst)
            
    
    
    
    return fnl


def  D_prnt(text):
    txt=dec(text.split(" "))

    txxt=""
    for q in range(len(txt)):
        txxt=f"{txxt} {txt[q]}"

    print(txxt)
    return 0
    

ask()

            




            











def inp():
   try:
    word=input("Enter A Word to check if it is plaindrome :")  
    rev(word)

    
   except ValueError:
      print("Invalid Input")


def rev(word):
  b=word[::-1]
  chk(word,b)

def chk(word,b):
  
  if(word==b):
    pnt(b)

  else:
    pnterr(b)
    
    

def pnt(b):
  print(f"The Word {b} is plaindome")

def pnterr(b):
  print(f"The word {b} isn't plaindome")


  
inp()
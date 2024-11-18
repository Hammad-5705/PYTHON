#   Create a program capable of displaying questions to the user like KBC.
#   Use List data type to store the questions and their correct answers.
#   Display the final amount the person is taking home after playing the game.


ques=[ 
        "Which statement stops loop?",
      ["Stop","End","Break","Pause"],

      "What is statement terminator?",
      ["*","#",":",";"],

      "What is integer?",
      ["4","e","5.5","!"],

      "Which is use to get value?",
      ["len()","append()","input()","print()"],

      "Which is correct?",
      ["a=1","1=a","1==a","a==1"],

      ]

ans=[0,1,2,3,4,5]
num=0
i=0
ii=-1
z=1

while(i<len(ques)):
    while z<=5:
        print("Q#",z,":    ",ques[i])
        print("\n\n",ques[i+1])
        break

    

    ans[ii]=input("Enter your Answer : ")


    if(z==1):
        if(ans[ii]=='C' or ans[ii]=='c'):
            num=num+1

    elif(z==2):
        if(ans[ii]=='D' or ans[ii]=='d'):
            num=num+1

    elif(z==3):
        if(ans[ii]=='a' or ans[ii]=='A'):
         num=num+1

    elif(z==4):
        if(ans[ii]=='C' or ans[ii]=='c'):
          num=num+1

    elif(z==5):
        if(ans[ii]=='A' or ans[ii]=='a'):
                 num=num+1

    i=i+2
    ii=ii+1
    z+=1



if(num==0):
   print("Unfortunatly You LosT")

elif(num==1):
   print("Congratulations....You Won RS.1000")

elif(num==2):
   print("Congratulations....You Won RS.2000")

elif(num==3):
   print("Congratulations....You Won RS.3000")

elif(num==4):
   print("Congratulations....You Won RS.4000")   

elif(num==5):
   print("Congratulations....You Won RS.5000")

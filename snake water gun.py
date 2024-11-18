# Snake Water Gun
# Snake, Water and Gun is a variation of the children's game "rock-paper-scissors" 
# where players use hand gestures to represent a snake, water, or a gun. 
# The gun beats the snake, the water beats the gun, and the snake beats the water. 
# Write a python program to create a Snake Water Gun game in Python using if-else statements. 
# Do not create any fancy GUI. 
# Use proper functions to check for win.

import random

def comp_inp():
        print("Its Computer\'s Turn\n")
        c=random.choice([0,1,2])
        return c


def user_inp():

    try:
        print("Its your turn")
        u=int(input("Choose 0 for Snake 1 for Water and 2 for Gun : "))
        return u

    except:
        raise ValueError

def game():
    a=user_inp()
    b=comp_inp()
    chk(a,b)    

def ret(x):
    if x=='0':
        x="Snake"
        return x

    elif x=='1':
        x="Water"
        return x

    elif x=='2':
        x="Gun"
        return x

def get_values(a,b):

    a=ret(a)
    b=ret(b)
    l1=[a,b]
    return l1
    
    

def pnt_D(a,b):
    a=str(a)
    b=str(b)
    l2=get_values(a,b)
    print(f"Game Draw\nYou choose {l2[0]} \nComputer Choose {l2[1]} \n Choose Again:\n\n\n ")
    game()

def pnt_W(a,b):
    a=str(a)
    b=str(b)
    l2=get_values(a,b)
    print(f"\n\n\nYou Win \nYou choose {l2[0]} \nComputer Choose {l2[1]}")

def pnt_L(a,b):
    a=str(a)
    b=str(b)
    l2=get_values(a,b)
    print(f"\n\n\nYou Lose \nYou choose {l2[0]} \nComputer Choose {l2[1]}")


def chk(a,b):

    l=[
        ["Draw","Win","Lose"],
        ["Lose","Draw","Win"],
        ["Win","Lose","Draw"]
    ]    

    if l[a][b]=="Draw":
        pnt_D(a,b)

    elif l[a][b]=="Win":
        pnt_W(a,b)

    elif l[a][b]=="Lose":
        pnt_L(a,b)
        

    

print("\n\n\nWelcome to Snake Water Gun game")
print("The Rules of game is simple")
print("The gun beats the snake, the water beats the gun, and the snake beats the water.")
print("Lets start\n\n\n")
game()
# Write a program to clear the clutter inside a folder on your computer. 
# You should use os module to rename all the png images from 1.png all the way till n.png 
# where n is the number of png files in that folder. 
# For example:
# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png
# Do the same for other file formats also.

import os
os.chdir("C:/Cources/pthn/garbage")



def fx():
    nme=os.listdir("C:/Cources/pthn/garbage")
    fnl=set()

    for i in nme:
        ind=i.index(".")
        n=i[ind:]
        fnl.add(n)
    fnl=list(fnl)

    for r in range(len(fnl)):
        if fnl[r] in i:
            change(i)


    

        

def change(i):
    ii=int(1)
    ind=i.index(".")
    n=i[ind:]
    os.rename(i,str(ii)+n)
    ii+=1
       

fx()
# Problem Statement:
# Create a Python class Rectangle to represent a rectangle. 
# Overload the following operators to perform operations on rectangles:

# + Operator: Combine two rectangles. The resulting rectangle should have:

# Width = sum of the widths of both rectangles.
# Height = sum of the heights of both rectangles.
# < Operator: Compare two rectangles. The comparison should be based on their areas. 
# A rectangle is smaller than another if its area is smaller.

# == Operator: Check if two rectangles are equal. 
# Two rectangles are equal if their widths and heights are the same.

# Instructions:
# Create a class Rectangle with attributes for width and height.
# Define the __add__, __lt__, and __eq__ methods for operator overloading.
# Write a __str__ method to display the rectangle dimensions in the format:
# "Rectangle(width=x, height=y)".

class Rectangle:
    def __init__(self,a,b):
        self.width=a
        self.height=b
        self.area=int(self.width)*(self.height)


    def __add__(self,x):
        return Rectangle(self.width+x.width , self.height+x.height)
    
    def __lt__(self,x):
        if self.area<x.area:
            return self.area < x.area
    
    def __eq__(self, x):
        if self.area==x.area:
            return self.area==x.area
        
        
    
rec1=Rectangle(9,3)
rec2=Rectangle(2,4)
print(rec1+rec2)
if rec1<rec2:
    print("rec 2 is greater")

elif rec1==rec2:
    print("rec1 and rec2 are Equal")

else:
    print("rec 1 is greater")



    

    



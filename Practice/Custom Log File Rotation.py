 # Write a program that monitors a file's size. 
# When it exceeds a certain size (e.g., 1MB), truncate the file, 
# move the contents to a backup file, and start fresh. 
# Implement this with the seek() and truncate() functions.

import os

size=os.stat('C:/Cources/pthn/Practice/file.txt')
size=size.st_size
size=size/1024
print(size)

if size>1:
    with open("C:/Cources/pthn/Practice/file.txt",'r') as f:
        f.seek(1024)
        text=f.read()

    with open("C:/Cources/pthn/Practice/extended_file.txt",'w') as f:
        f.write(text)

    with open("C:/Cources/pthn/Practice/file.txt",'r+') as f:
        f.truncate(1024)
        
        


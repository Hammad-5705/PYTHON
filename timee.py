# Problem Statement:
# Write a Python program that measures the execution time of a simple operation, 
# pauses the program for a few seconds using time.sleep(), 
# and displays the start time, 
# end time, and elapsed time in a formatted way.

# Requirements:
# Record the start time using time.time().
# Perform an operation: Write a loop that calculates the sum of numbers from 1 to 10 million.
# Pause the program for 3 seconds using time.sleep().
# Record the end time after the pause.
# Calculate and display the following:
# Elapsed time: Total time taken to execute the program, including the pause.
# Formatted start and end times: Display times in the format YYYY-MM-DD HH:MM:SS using time.strftime().


import time



start=time.time()
sum=0
for i in range (1000000):
    sum=sum+i

time.sleep(3)

end=time.time()
elapsed=end-start
print(f"starting time = {time.strftime("%Y-%m-%d %H:%M:%S" , time.localtime(start))}\nending time = {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end))}\nElapsed = {elapsed}")
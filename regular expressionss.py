# You need to validate and extract phone numbers from a given text. The phone numbers can be in the following formats:

# (123) 456-7890
# 123-456-7890
# 123.456.7890
# 1234567890
# +31636363634
# 075-63546725
# Instructions
# Extract Phone Numbers: 
# Write a function that takes a string of text and returns a list of all valid phone numbers found in that text.

# Validate Format: Ensure that the extracted phone numbers match one of the specified formats.

# Avoid False Matches: Make sure that the function does not include any invalid phone numbers.

# Example Input and Output
# Input:

# python
# text = """  
# Please contact us at (123) 456-7890 or 123-456-7890.   
# You can also reach us at 123.456.7890 or 1234567890.   
# For international inquiries, call +31636363634 or local support at 075-63546725.   
# Thanks!  
# """  
# Output:

# python
# ['(123) 456-7890', '123-456-7890', '123.456.7890', '1234567890', '+31636363634', '075-63546725']  
# Hints
# You can use the re module to define a regex pattern for matching the phone number formats.
# You might want to utilize re.findall() to get all matches from the text.
# Test your function with various input strings to ensure it captures all valid formats correctly.
# Additional Challenge
# Modify your function to also check if the numbers are in a specified country code 
# (e.g., only allow phone numbers that start with +31 for Netherlands).

import re

text="""Contact us for inquiries:  
- Customer Service: (0300) 123-4567  
- Sales Department: 0321-765-4321  
- Technical Support: 0345.987.6543  
- Office Hours: 0214567890  
- Emergency Contact: +92300-1234567  
- Head Office: 0423456789  
- After Sales: +9242.9876543  
- Islamabad Branch: +92345 678 9012  
- Lahore Branch: 03011234567  
- Karachi Office: +92321234567  
- General Inquiries: 0321-111-2222  
4438767
- Toll Free: 0800-12345 

For more information, please reach us at 021-1234567 or email us at info@example.com."""  

# pattern=r"^(0|92)+(300|301|302|303|304|305|306|307|308|309|310|311|312|313|314|315|316|317|318|319|320|321|322|323|324|325|326|327|328|329|330|331|332|333|334|335|336|337|338|339|340|341|342|343|344|345|346|347|348|349|355|370)"

pattern = r'\(?\d{3,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}|\+\d{2,3}[\s.-]?\d{3}[\s.-]?\d{7}|\d{11}|\d{4}[\s.-]?\d{4}'  

matches=re.findall(pattern,text)

for match in matches:
    print(match)
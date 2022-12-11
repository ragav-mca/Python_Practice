"""
Validate user input for username. Conditions - username length should be between 4 and 8, 
should not start with a number, should not start or end with '_', and only alphabets, numbers
and '_' is allowed.
When the user enters an username, you should print all possible errors in the username.
For eg - if input is 1b%  - the output should be 'Username length should be >4 <8, 
no numeric at the start and no special chars allowed' 
"""

username=input("Enter the name: ")
a = len(username)
spl_char = "~`!#$%^&*()-+=;:<>,./@|[]"
b = 1
c = 1
if a < 4 or a > 8:
    b=False
    print("The username length is < than 4 or > than 8")
 
if username[0].isdigit():
    b=False
    print("The username starts with number")
    
if username.startswith("_"):
    b=False
    print("The username starts with underscore")
    
if username.endswith("_"):
    b=False
    print("The username ends with underscore")

for i in range(len(spl_char)):
    if spl_char[i] in username:
        b=False
        c=False
if c==False:
    print("The username consists of special character")

if b==False:
    print("Username is Invalid")
else:
    print("Username is valid")
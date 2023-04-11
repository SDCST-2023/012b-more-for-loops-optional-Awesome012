#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]

awesome = True
while awesome:
    cool1 = 98
    cool2 = 1002
    usernameinput = input("enter username: ")
    passwordinput = input("enter password: ")
    if usernameinput in users:
        cool1 = users.index(usernameinput)
    if passwordinput in passwords:
        cool2 = passwords.index(passwordinput)
    if cool1 == cool2:
        awesome = False
    else: 
        print("try again\n")
        
print("welcome user")
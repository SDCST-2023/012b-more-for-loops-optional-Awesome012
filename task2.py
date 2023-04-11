#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = ""
expectedPassword = ""

guess = 0
while expectedUsername != "systemadmin" and expectedPassword != "master" and guess < 3:
    expectedUsername = input("enter username: ")
    expectedPassword = input("enter password: ")
    if expectedUsername != "systemadmin" or expectedPassword != "master":
        print("access denied \n")
        guess = guess + 1
if guess < 3:
    print("access granted")
else:
    print("to many attempts\naccess denied")
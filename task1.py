#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
import random

def rand1():
    random1 = random.randint(1,100)
    random1 = float(random1)
    guess = 0
    number = 0
    number = int(number)
    while guess != random1 and number < 10:
        awesome = 10 - number
        awesome = int(awesome)
        print(f"you have {awesome} guesses left")
        guess = input("guess the number: ")
        guess = float(guess)
        if guess > random1:
            print("that number is more than the random one\n")
            number = number + 1
        if guess < random1:
            print("that number is lower than the random one\n")
            number = number + 1
        if guess == random1:
            print(f"you got it! that was the number!")
        if guess != random1 or guess == 0:
            print("guess again!")
    if number >= 10:
        print("nevermind, you ran out of guesses :(")


if __name__ == "__main__":
    rand1()
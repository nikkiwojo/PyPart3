#Asks the user to input a number
print("Please enter a number between 0 and 10.")
player_number = input()

#Generates a random number between 1 and 10
from random import randrange
computer_number = randrange(1,10,1)

#States the two numbers being compared
print("Your number was: ", player_number)
print("The computer's number was: ", computer_number)

#The function compares the two numbers and determines which is larger
def higher_or_lower(x, y):
    if(x>y):
        print("Sorry, your number was too big.")
    elif(x<y):
        print("Sorry, your number was too small.")
    else:
        print("Congratulations, you win! :)")

higher_or_lower(int(player_number), computer_number)

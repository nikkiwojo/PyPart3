#Asks the user for their name, inputs as string variable
def name_input():
    print("Please enter your name. ")
    provided_name = input()
    return provided_name

#Inserts the name into the greeting
def greet(name):
    print("Hello! How are you, ", name, "?")

greet(name_input())

#Allows the user to choose a language.
def language_input():
    print("Please choose a language: \n A. Spanish \n B. French \n C. German")
    language = input()
    return language

#asks the user for their name in the chosen language
selection = language_input()

if (selection == "A" or selection == "a"):
    print("What is your name in Spanish?")
    new_name = input()
    print("Hola, ", new_name, "!")
elif (selection == "B" or selection == "b"):
    print("What is your name in French?")
    new_name = input()
    print("Bonjour, ", new_name, "!")
elif (selection =="C" or selection == "c"):
    print("What is your name in German?")
    new_name = input()
    print("Hallo, ", new_name, "!")

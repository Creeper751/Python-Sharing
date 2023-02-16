from os import system as cmd #Shell command function from os
running = True #Declare var for while loop below
activateDebugSequence = True #manual control over whether the debug question will be asked
print("Welcome the Python3.11 Interactive Code Testing")# Intro
cmd('cat ~/PycharmProjects/LearningPython/banner')# PyCode Testing inc. | Use shell command since print() doesn't like the weird banner chars
print() # print newline since /n is not in banner
if activateDebugSequence and input("Would you like to activate debug mode? [y/N]: ").lower() == "y": #debug mode if needed
        debug = True
def Session1(): #declare Session 1. Is main code workspace
    print("Session 1 works!")
while running: #while loop for error exeption
    try:
        Session_Ask = int(input("Which coding session would you like?: "))
        if Session_Ask == 1:
            running = False
            Session1()
        elif Session_Ask > 1:
            print("WIP")
    except ValueError:
        print("Not a valid number. Please try Again.")
    finally:
        print("Thank you for using PyCode Testing inc! Have a nice day!")


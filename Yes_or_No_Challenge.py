import os
os.system('cls')

import pyfiglet
ascii = pyfiglet.figlet_format("Yes or No Challenge")
green = "\033[92m" + ascii + "\033[0m"
print(green)

print("Welcome to Yes or No Challenge!")
print("INSTRUCTIONS:  I will say a question and you have to answer in yes or no! I will not say proper questions as this is a challenge, so be ready!")
print()

while True:
    firstQuestion = input("FIRST QUESTION: Will you choose this food: ")
    if firstQuestion == "Yes" or firstQuestion == "yes":
        print("HAHA! Sugar!")
        break
    elif firstQuestion == "No" or firstQuestion == "no":
        print("Great! Always avoid: Sugar")
        break
    else:
        print("False! You didn't answer in yes or no! Must be a yes or no! Try again!")

while True:
    secondQuestion = input("SECOND QUESTION: Will you choose this house: ")
    if secondQuestion == "Yes" or secondQuestion == "yes":
        print("You're so lucky! Answer is: Luxury Home!")
        break
    elif secondQuestion == "No" or secondQuestion == "no":
        print("Why, you don't want a luxury home?")
        break
    else:
        print("False! You didn't answer in yes or no! Must be a yes or no! Try again!")

while True:
    finalQuestion = input("FINAL QUESTION: Will you choose this car: ")
    if finalQuestion == "Yes" or finalQuestion == "yes":
        print("SHEER LUCK!! You've got a LAMBOGHINI!!!!!!")
        break
    elif finalQuestion == "No" or finalQuestion == "no":
        print("LOST IT, HA! You've lost a lambogrini!")
        break
    else:
        print("False! You didn't answer in yes or no! Must be a yes or no! Try again!")

print("That's it! You've finished the challenge! Have a nice day! Goodbye!!")
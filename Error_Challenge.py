import os
os.system('cls')

import pyfiglet
ascii = pyfiglet.figlet_format("Error Challenge")
red = "\033[31m" + ascii + "\033[0m"
print(red)

print("Welcome to Error Challenge!")
print("INSTRUSTIONS: I will say an error and you have to guess the type of error! I may not say proper errors as this is a challenge, so be ready!")
print()
while True:
    firstError = input("FIRST ERROR: What is the type of this error: 'print('Hello World')' ")
    if firstError.lower() == "syntax error":
        print("Correct! That's a \033[31mSyntax Error!\033[0m")
        break
    elif firstError.lower() == "runtime error":
        print("Incorrect! That's not a Runtime Error!")
        break
    else:
        print("False! Try again with \033[31mSyntax Error\033[0m or \033[31mRuntime Error!\033[0m")
while True:
    secondError = input("SECOND ERROR: What is the type of this error: 'x = 5 + 'Hello'' ")
    if secondError.lower() == "type error":
        print("Correct! That's a \033[31mType Error!\033[0m")
        break
    elif secondError.lower() == "syntax error":
        print("Incorrect! That's not a \033[31mSyntax Error!\033[0m")
        break
    else:
        print("False! Try again with \033[31mType Error\033[0m or \033[31mSyntax Error!\033[0m")
while True:
    finalError = input("FINAL ERROR: What is the type of this error: 'print(Hello World)' ")
    if finalError.lower() == "name error":
        print("Correct! That's a \033[31mName Error!\033[0m")
        break
    elif finalError.lower() == "syntax error":
        print("Incorrect! That's not a \033[31mSyntax Error!\033[0m")
        break
    else:
        print("False! Try again with \033[31mName Error\033[0m or \033[31mSyntax Error!\033[0m")
print("That's it! You've finished the challenge! Have a nice day! Goodbye!!")
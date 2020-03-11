import time
import random

print()
print("Welcome to Hangman.")
print ("Type Automatic to play the computer, or Manual to enter your own word:")
mode = input()
print()

if mode == 'automatic' or mode == 'Automatic':
    print ("Playing Automatic mode. Enter level (Easy or Difficult):")
    level = input()
    print()

    print ("Choosing word...")
    f = open("%s.txt" %(level.lower()), "r")
    lineCount = 0
    for x in f:
        lineCount +=1
    f.seek(0)
    random.seed(10)
    rand = random.randint(1,lineCount)
    counter = 0
    for y in f:
        counter +=1
        if counter == rand:
            word = y
    f.close()
    time.sleep(2)

    print ("Word has been chosen:")
    print(word)
elif mode == 'manual' or mode == 'Manual':
    print ("Playing Manual mode. Enter your word:")
    manualWord = input()
else:
    print("Invalid input. Please try again") 

import time
import random

def validatorFunc(funcInput, stage):
    if stage == 'mode':
        if funcInput == 'automatic' or funcInput == 'Automatic' or funcInput == 'manual' or funcInput == 'Manual':
            return funcInput
        else:
            print ()
            print("Invalid input. Please try again:")
            funcInput = input()
            return validatorFunc(funcInput, 'mode')
    elif stage == 'difficulty':
        if funcInput == 'easy' or funcInput == 'Easy' or funcInput == 'Difficult' or funcInput == 'difficult':
            return funcInput
        else:
            print ()
            print("Invalid input. Please try again:")
            funcInput = input()
            return validatorFunc(funcInput, 'difficulty')

def random_line(afile):
    line = next(afile)
    for num, aline in enumerate(afile, 2):
      if random.randrange(num): continue
      line = aline
    return line


print()
print("Welcome to Hangman.")
print ("Type Automatic to play the computer, or Manual to enter your own word:")
inputMode = input()

valMode = validatorFunc(inputMode, 'mode')
print()

if valMode == 'automatic' or valMode == 'Automatic':
    print ("Playing Automatic mode. Enter level (Easy or Difficult):")
    level = input()
    valLevel = validatorFunc(level, 'difficulty')
    print()

    print ("Choosing word...")
    f = open("%s.txt" %(valLevel.lower()), "r")
    word = random_line(f)
    f.close()
    time.sleep(2)

    print ("Word has been chosen:")
    print(word)
elif valMode == 'manual' or valMode == 'Manual':
    print ("Playing Manual mode. Enter your word:")
    word = input()

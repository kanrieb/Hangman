import time
import random

#function to validator automatic/manual, easy/difficult user inputs
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

#chooses a random line containing a word from a txt file for Automatic mode
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

#word selection segment
if valMode == 'automatic' or valMode == 'Automatic':
    print ("Playing Automatic mode. Enter level (Easy or Difficult):")
    level = input()
    valLevel = validatorFunc(level, 'difficulty')
    print()
    print ("Choosing word...")
    f = open("%s.txt" %(valLevel.lower()), "r")
    word = random_line(f)[:-1]
    f.close()
    time.sleep(1)
    print ("Word has been chosen:")
elif valMode == 'manual' or valMode == 'Manual':
    print ("Playing Manual mode. Enter your word:")
    word = input()

#word has been chosen, game begins now
print('x' * len(word))
print()
if len(word) <= 4:
    lives = 5
elif len(word) >=5 or len(word) <= 8 :
    lives = 8
else:
    lives = 10 

print("You have %i lives. Please enter a letter:" %lives)

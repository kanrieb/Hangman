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
    if not word.isalpha():
        while not word.isalpha():
            print("Invalid word. Please try again:")
            word = input()

print() 

#word has been chosen, game begins now
print('*' * len(word))
newWord = '*' * len(word)
if len(word) <= 4:
    lives = 5
elif len(word) >=5 or len(word) <= 8 :
    lives = 8
else:
    lives = 10 

#restrict letters already used
#show instances of one letter
#remove lives if wrong
correctLetters = []
usedLetters = []

while lives != 0:
    print("You have %i lives. Guess a letter and press enter:" %lives)
    letter = input()
    if len(letter) != 1 or not letter.isalpha(): 
        while len(letter) != 1 or not letter.isalpha():
            print("Invalid input. Please enter another letter:")
            letter = input().lower()
    print()
    letterCount = word.count(letter)
    if letterCount != 0:
        print("Your letter is in the word.")
        correctLetters += letter
        counter = 0
        oldWord = newWord
        newWord = ''
        for a in word:
            if letter == a:
                print(a, end='')
                newWord += a
            else: 
                print(oldWord[counter], end = '')
                newWord += oldWord[counter]
            counter += 1
        print()
    else: 
        print("Your letter is not found in the word. Please try again.")
        print(newWord)
        lives -= 1
    
#    usedLetters += letter

print("You are out of lives.")
print("GAME OVER")

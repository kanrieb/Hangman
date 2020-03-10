import time

print("Welcome to Hangman.")
print ("Type Automatic to play the computer, or Manual to enter your own word:")
mode = input()
print()

if mode == 'automatic' or mode == 'Automatic':
    print ("Playing Automatic mode.")
    time.sleep(1)
    print ("Choosing word...")
    time.sleep(2)
    print ("Word has been chosen:")
elif mode == 'manual' or mode == 'Manual':
    print ("Playing Manual mode. Enter your word:")
    manualWord = input()
else:
    print("Invalid input. Please try again") 

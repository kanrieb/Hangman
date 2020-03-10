print("Welcome to Hangman.")
print ("Type Automatic to play the computer, or Manual to enter your own word:")
mode = input()

if mode == 'manual' or mode == 'Manual':
    print ("Playing Manual mode. Enter your word:")
elif mode == 'automatic' or mode == 'Automatic':
    print ("Playing Automatic mode.")
    print ("Generating word...")

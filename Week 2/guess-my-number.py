'''
Please think of a number between 0 and 100!
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
'''

print("Please think of a number between 0 and 100!")
high = 100
low = 0
guess = (high + low) // 2
found = False

while not found:
    print("Is your secret number %d?" % (guess))
    op = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if op == "c":
        found = True
    elif op == "l":
        low = guess
    elif op == "h":
        high = guess
    else:
        print("Sorry, I did not understand your input.")

    guess = (high + low) // 2

print("Game over. Your secret number was: %d" % guess)

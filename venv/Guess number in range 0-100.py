print("Please think of a number between 0 and 100!")
low = 0
high = 100
middle = int((high - low) // 2)
print("Is your secret number " + str(middle) + "?")
guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while guess != "c":
    if guess == "h":
        low = middle
        middle = int((high + low) / 2)
    elif guess == "l":
        high = middle
        middle = int((high + low) / 2)
    else:
        print("Sorry, I did not understand your input.")
    print("Is your secret number " + str(middle) + "?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
print("Game over. Your secret number was: " + str(middle))
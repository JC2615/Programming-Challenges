high = 101
low = 0
guess = 0
input("Think of a number between 0 and 100 then press enter. ")

while True:
    guess = (high + low) // 2
    feedback = input("Is your number " + str(guess) + "?" + " If it's right, press 'y'. If it's too low, press 'l'. If it's too high, press 'h'. \n")
    if feedback == 'y':
        print("Awesome! I guessed your number.")
        break
    elif feedback == 'l':
        low = guess
    elif feedback == 'h':
        high = guess
    else:
        print("Sorry, your input is invalid. Please try again.")
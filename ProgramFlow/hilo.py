low = 1
high = 1000

print("Please think of a number between {} and {}.".format(low, high))
input("Press ENTER to start.")

guesses = 1
while True:
    guess = low + (high - low) // 2  # formula for binary chop
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct. "
                     .format(guess)).casefold()

    if high_low == "h":
        # Guess higher. The low end of the range becomes one greater than the guess.
        # pass # placeholder code so that errors do not occur when no code exists in a block
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, or c.")

    guesses += 1

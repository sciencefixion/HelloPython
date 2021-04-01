import random

# my solution
highest = 10
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing

"""
Challenge: Modify the program to use a while loop, to allow the player to keep guessing.
The program should let the player know whether to guess higher or lower, 
and should print a message when the guess is correct.
It already does that, but I suggest you don't worry about printing a different message, 
if they get the correct answer on their first guess.
We'll look at counting the number of guesses later.
A correct guess will terminate the program.
As an optional extra, allow the player to quit by entering 0 (zero) for their guess.
"""

print("Please guess a number between 1 and {}: ".format(highest))
print("Type 0 to quit.")
guess = int(input())


if guess == answer:
    print("You got it first time")
else:
    while guess != answer:
        if guess == 0:
            print("The machines have won! Goodbye!")
            break
        elif guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it")
            break

# alt DRY solution:

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing
guess = 0 # initialize to any number that doesn't equal the answer
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("Well done, you guessed it.")
        break
    else:
        if guess < answer:
            print("Please guess higher.")
        else: # guess must be greater than answer
            print("Please guess lower.")

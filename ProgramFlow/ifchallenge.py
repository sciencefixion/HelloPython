name = input("Please enter your name: ")

age = int(input("How old are you? "))

if 18 <= age < 31:
    print("Welcome {0}, aboard the ship to Good Time Island!".format(name))
else:
    print("Apparently {0}, your age is too old or young to enjoy pleasure. Please grow older or younger to join us.".format(name))

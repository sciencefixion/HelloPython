# index positions:
#         012345678901234
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])

# Strings in Python are zero indexed
# look up sequence data types

# MINI CHALLENGE: Add some code to the program so that it prints out "we win".
# Each character should get the characters from the parrot string, using indexing.
# The "w" is already printed out, so you just need to print the remaining 5 characters.
# With the text that is already being printed, the final output from the program should be:

# Norwegian Blue
# w
# e
#
# w
# i
# n

print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
print(parrot[-1])
print(parrot[-14])

# Mini mini Challenge: print the same output as the above challenge using negative indexing

print()
print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

# negative indexes can be obtained by subtracting the total length of the string from the positive index
print()
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

# Slicing

print(parrot[0:6])  # Norweg
# from index 0 up to but not including index 6
print(parrot[3:5])
print(parrot[0:9])
# start value defaults to the start of the sequence
print(parrot[:9])
# index 14 is the stop value, the stop value is the default if no end index is specified
print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

letters = "abcdefghijklmnopqrstuvwxyz"

# Slicing with negative numbers
print(parrot[-14:-8])
print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl

# Using a step in a slice
print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,223,372,036,854,775,807"
print(number[1::4])
number = "9,223;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])
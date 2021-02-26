letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)
backwards2 = letters[25::-1]
print(backwards2)
# with a negative step the start and stop defaults are reversed

backwards3 = letters[::-1]
print(backwards3)

# Challenge: Using the letters string add some code to create the following slices
# create a slice that produces the characters "qpo"
# slice the string to produce "edcba"
# slice the string to produce the last 8 characters in reverse order

slice1 = letters[-10:-13:-1]
slice2 = letters[-22::-1]
slice3 = letters[-1:-9:-1]
print(slice1)
print(slice2)
print(slice3)

# alternate solution

print(letters[16:13:-1])
print(letters[4::-1])
print(letters[:-9:-1])

# defaults for the stop and step values
print(letters[-4:])
print(letters[-1:])
# defaults for the start and step
print(letters[:1])
print(letters[0])


splitString = "This string has been\nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
# or
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")
# or
print("""The pet shop owner said "No, no, \
'e's uh,... he's resting". """)

anotherSplitString = """This string has been \
split over \
several \
lines"""
# the backslash escapes the end of the line so anotherSplitString is all on one line
print(anotherSplitString)

#preferred method for escaping escape chars
print("C:\\Users\\timbuchalka\\notes.txt")
#raw string, this is not preferred
print(r"C:\Users\timbuchalka\notes.txt")
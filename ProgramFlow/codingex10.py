"""
Modify the code so that it stops printing when it reaches a number greater than zero that's exactly divisible by 11.
That number should be the last value printed.
Reminder: If a value, x, is divisible by 11 then x % 11 will be zero.
The code should print the same values as it currently does, but stop after printing a number that's also divisible by 11.
Hint: 0 is exactly divisible by every number, so your solution will need to allow for that.
"""

# starter code
# for i in range(0, 100, 7):
#     print(i)

# my first solution
for i in range(0, 100, 7):
    if i > 0 and (i % 11 == 0):
        print(i)
        break
    else:
        print(i)

# DRY solution
for i in range(0, 100, 7):
    print(i)
    if i > 0 and i % 11 == 0:
        break

"""
Write a program to print out all the numbers from 0 to 100 that are divisible by 7.
Note that zero is considered to be divisible by all other integers, so your output should include zero.
"""

# using step
for i in range(0, 101, 7):
    print(i)

# using slice
for i in range(101)[::7]:
    print(i)
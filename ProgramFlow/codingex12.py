"""
Augmented Assignment in a loop
Early computers could only perform addition. In order to multiply one number by another,
They performed repeated addition.
For example, 5 * 8 was performed by adding 5 eight times.

Use a for loop, and augmented assignment to give answer the result of multiplying number by multiplier.
"""

# starter code
number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(multiplier):
    answer += number

print(answer)
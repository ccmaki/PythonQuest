# Write the code ↓ to read the user's input for a non-negative integer.
# Be cautious when reading input of various data types.
print("FACTORIAL CALCULATOR FOR ALF")
number = int(input("Please, enter a non-negative integer: "))
while (number < 0):
    print("Invalid input")
    number = int(input("Please, enter a non-negative integer: "))
output = number
# Write the code ↓ to calculate the factorial of the user-defined integer using a loop.
factorial = 1
for number in range (number, 0, -1):
    factorial = factorial * number

# Write the code ↓ to display the factorial result.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The factorial of %d is: %d" % (output, factorial))




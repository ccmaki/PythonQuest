# Write the code ↓ to read user's input for two operands and selected operation.
# NOTE: The two operands must be read as floats.
print("SIMPLE CALCULATOR FOR ALF\n")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, x, /): ")[0]
answer = 0.0
correct = 0
# Write the code ↓ to perform the calculations based on the selected operation.
if operator == '+':
    answer = first + second
elif operator == '-':
    answer = first - second
elif operator == 'x':
    answer = first * second
elif operator == '/':
    answer = first / second
else:
    print("\nInvalid input")
    correct = 1
    

# Write the code ↓ to display the result.
# Select and employ a string concatenation method based on your personal preference and comfort level.
if correct == 0:
    print("\nThe result of %.1f %s %.1f is %.1f" % (first, operator, second, answer))







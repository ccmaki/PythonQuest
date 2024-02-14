import math

# Write the code ↓ to read the lengths of the two shorter sides of a right-angled triangle from the user.
# Be cautious when reading input of various data types.
print("HYPOTENUSE CALCULATOR FOR ALF")

side1 = float(input("Please, enter the length of side A: "))
while (side1 < 0):
    print("Invalid input")
    side1 = float(input("Please, enter the length of side A: "))

side2 = float(input("Please, enter the length of side B: "))
while (side2 < 0):
    print("Invalid input")
    side2 = float(input("Please, enter the length of side B: "))

# Write the code ↓ to calculate the hypotenuse using the Pythagorean theorem.
# The Pythagorean theorem: c^2 = a^2 + b^2, where c is the hypotenuse.
hypotenuse = math.sqrt((side1*side1) + (side2*side2))

# Write the code ↓ to display the calculated hypotenuse.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The hypotenuse of the right-angled triangle is: %.2f" % (hypotenuse))

# Write the code ↓ to read user's input.
# Be cautious when reading input of various data types.
print("PUP Enrollment Form\n")
name = input("Enter your full name: ")
age = input("Enter your age: ")
average = float(input("Enter your previous weighted average: "))
is_member = input("Are you a member of the AWS Cloud CLub: ").lower() == "yes"



# Write the code ↓ to display the user's personal information.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("\n")
print("Your Enrollment form")
print("Name: "+name)
print("Age: "+age)
print("GWA:",average)
if is_member == 1:
    print("AWStraunot: True")
else:
    print("AWStraunot: False")





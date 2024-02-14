# Write the code ↓ to prompt the user to enter a word.
# Be cautious when reading input of various data types.
print("VOWEL COUNTER FOR ALF\n")
word = input("Please, enter a word/s to check: ")


# Write the code ↓ to count the number of vowels in the entered word.
# Utilize string functions to iterate through the characters and identify vowels.
lower = word.lower()
a_count = lower.count('a')
e_count = lower.count('e')
i_count = lower.count('i')
o_count = lower.count('o')
u_count = lower.count('u')
total = a_count + e_count + i_count + o_count + u_count

# Write the code ↓ to display the count of vowels in the word.
# Select and employ a string concatenation method based on your personal preference and comfort level.
print("The number of vowels in '%s' is: %d" % (word, total))

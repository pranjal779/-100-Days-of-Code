# Hard Version
# When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:

# x$d24g\*f9

# And every time you generate a password, the positions of the symbols, numbers, and letters are different. This will make the password more difficult for hackers to crack.

# The essential skill of a good programmer is using Google to find what you need. Your brain is for thinking, not memorising functions! You will need to Google to solve this project on the hard level. If you get stuck, check the hint below for what to Google.

# Hint 2
# Try googling: "How to shuffle items in a List in Python"

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


passwordList = []
for letter in range(0, nr_letters):
    # passwordList += random.choice(letters)
    # or
    passwordList.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    # passwordList += random.choice(symbols)
    # or
    passwordList.append(random.choice(symbols))


for number in range(0, nr_numbers):
    # passwordList += random.choice(numbers)
    # or
    passwordList.append(random.choice(numbers))


print(passwordList)

random.shuffle(passwordList)
print(passwordList)


password = ""
for echar in passwordList:
    password += echar

print(f"Your password is: {password}")


# example output:
# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 4
# How many symbols would you like?
# 2
# How many numbers would you like?
# 3
# ['x', 'c', 'Q', 'B', '#', ')', '3', '2', '7']
# ['B', 'Q', '2', 'x', '3', 'c', ')', '7', '#']
# Your password is: BQ2x3c)7#

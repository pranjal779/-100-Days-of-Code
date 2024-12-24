import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# easy version
# Generate the password in sequence. Letters, then symbols, then numbers. If the user wants

# 4 letters 2 symbols and 3 numbers then the password might look like this:

# fgdx$\*924
password = ""
for letter in range(0, nr_letters):
    password += random.choice(letters)

# Sample output:
# 4
# UKeh

for symbol in range(0, nr_symbols):
    password += random.choice(symbols)

# example Output:
# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 4
# How many symbols would you like?
# 3
# Ifvz$#!

for number in range(0, nr_numbers):
    password += random.choice(numbers)

# example Output:
# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 4
# How many symbols would you like?
# 2
# How many numbers would you like?
# 3
# EReC&%672

print(password)

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# Easy way
# import random
# letter.random.choice {len of input}
# + numbers.random {len of input}
# + symbols.random {len of input}
# print them without space


password = ""
#
for char in range(0, nr_letters):
    password += random.choice(letters)


for symbls in range(0, nr_symbols):
    password += random.choice(symbols)

for nums in range(0, nr_numbers):
    password += random.choice(numbers)

print(password)
#
# # Output:
# # Welcome to the PyPassword Generator!
# # How many letters would you like in your password?
# # 4
# # How many symbols would you like?
# # 2
# # How many numbers would you like?
# # 2
# # kJdk)&78
# #
# # Process finished with exit code 0


passwordList = []
for eletter in range(0, nr_letters):
    passwordList.append(random.choice(letters))

for eSymbol in range(0, nr_symbols):
    passwordList.append(random.choice(symbols))

for eNumber in range(0, nr_numbers):
    passwordList.append(random.choice(numbers))


strPasswordList = ""
for eachPassword in passwordList:
    strPasswordList += eachPassword

print(strPasswordList)

# Welcome to the PyPassword Generator!
# How many letters would you like in your password?
# 4
# How many symbols would you like?
# 4
# How many numbers would you like?
# 2
# MWTJ)(%!27
# yWtC*+!%90

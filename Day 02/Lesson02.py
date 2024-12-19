# len(12345) # Throws TypeError

len("12345")

print(type("hello"))
print(type(1234))
print(type(False))
print(type(1234.34))

# Type Conversion or Type Casting

int("1234")

print(int("12345") + int("45657"))

# print(int("abc") + int("1234")) # this will throw Value Error

print("Number of letters in your name: " +
      str(len((input("Enter your name")))))
#     print("Number of letters in your name: " + len(input("Enter your name")))
#           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TypeError: can only concatenate str (not "int") to str

# or

name_of_the_user = input("Name:")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int


height = 1.65
weight = 84

# Write your code here.
sq_height = height * height
# Calculate the bmi using weight and height.
bmi = (weight / sq_height)

print(bmi)

# 30.85399449035813


bmi02 = 84 / 1.65 ** 2

height = 1.65
weight = 84

# Write your code here.
sq_height = height * height
# Calculate the bmi using weight and height.
bmi = (weight / sq_height)

print(bmi)

# 30.85399449035813

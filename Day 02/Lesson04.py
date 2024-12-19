bmi02 = 84 / 1.65 ** 2

height = 1.65
weight = 84

# Write your code here.
sq_height = height * height
# Calculate the bmi using weight and height.
bmi = (weight / sq_height)

print(bmi)

# 30.85399449035813

print(int(bmi))

print(round(bmi))

# print(round(number, ndigits))
print(round(bmi, 2))


# Assignment Operators
score = 0

score += 1

print(score)

# f-strings

age = 12

print(f"I am {age} years old")

name = input("What is your name?")
print(f"Hello, {name}")

name02 = input("What is your name?")
print("Hello, " + name02)

# print("You are " + age + " years old")
#  threw this error
#     print("You are " + age + " years old")
#           ~~~~~~~~~~~^~~~~
# TypeError: can only concatenate str (not "int") to str

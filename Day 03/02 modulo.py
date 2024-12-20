# Even_number
inputted_number = int(input("Enter the number: "))

# Check Odd or Even
# Write some code using what you have learnt about the modulo operator and conditional checks in Python to check if the number in he input area is odd or even. If it's odd print out the word "Odd" otherwise printout "Even".

# check if the number is Even or not
if inputted_number % 2 == 0:
    print(f"{inputted_number} is Even.")
else:
    print(f"{inputted_number} is not Even.")


# Enter the number: 121
# 121 is not Even.

# Enter the number: 120
# 120 is Even.

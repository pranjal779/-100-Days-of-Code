print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")
    # next if will come here:

    wantPhoto = input(
        "Do you want a photo or not? Type y for Yes and n for No,")
    if wantPhoto == "y":
        # Add $3 to the bill
        bill += 3

    print(f"your final bill is {bill}")

else:
    print("Sorry you have to grow taller before you can ride.")

# Welcome to the rollercoaster!
# What is your height in cm? 126
# You can ride the rollercoaster
# What is your age? 27
# Please pay $12.
# Do you want a photo or not? Type y for Yes and n for No,y
# your final bill is 15
#
# Process finished with exit code 0

# You can write as many if statements as you need to check for different conditions that are unrelated to each other.
#  Compare the code blocks below:

# If/elif/else
# if <condition 1 is true>
#     <do A>
# elif <condition 2 is true>
#     <do B>
# else
#     <do C>
# Nested if statements
# if <condition 1 is true>
#     <do A>
#     if <condition 2 is true>
#         <do B>
#         if <condition 3 is true>
#             <do C>
# Multiple if statements
# if <condition 1 is true>
#     <do A>
# if <condition 2 is true>
#     <do B>
# if <condition 3 is true>
#     <do C>

# In the if/elif/else block, only one of A, B, or C can happen, because if/elif/else are mutually exclusive.
#  The first condition has to fail to go into the elif and the elif (or multiple elif) have to fail to go into the else.
#  Condition 2 is only checked if condition 1 is false.

# In the nested if statements, A, B and C can all happen, but conditions 1, 2 and 3 must all be true.
#  The computer will only check condition 2 if condition 1 is true.

# In the multiple if statements, A, B, and C can all happen. But they are completely independent of each other.
#  C can happen even if A and B don't. Every condition is checked, no matter the result of the others.

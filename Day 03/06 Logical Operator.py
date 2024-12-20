print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    # Free Ride for Age 45 to 55
    if age > 45 and age < 55:
        bill = 0
        print(
            f"Your Age is in between 45 and 55 you can ride for free and your total bill is {bill}")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


# Welcome to the rollercoaster!
# What is your height in cm? 154
# You can ride the rollercoaster!
# What is your age? 47
# Adult tickets are $12.
# Your Age is in between 45 and 55 you can ride for free and your total bill is 0
# Do you want a photo taken? Y or N. N
# Your final bill is $0
#
# Process finished with exit code 0


# Welcome to the rollercoaster!
# What is your height in cm? 144
# You can ride the rollercoaster!
# What is your age? 29
# Adult tickets are $12.
# Do you want a photo taken? Y or N. Y
# Your final bill is $15
#
# Process finished with exit code 0


# Solution:
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        # Or
        # 45 <= age <= 55
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


# calculating total tip
total_tip = 1.00 + (tip / 100)
print(total_tip)


# calculating total bill that needs to be paid
total_bill = bill * total_tip
print(total_bill)


# Calculating total Amount that needs to be paid by every one
individuals_amount = total_bill / people

print(round(individuals_amount, 2))

print(f"""The Bill amount is {round(bill, 2)}, you gave the tip of {round(tip, 2)}%, the total tip was {total_tip},
      The Total Bill amount is {round(total_bill, 2)}, and each person has to pay {(round(individuals_amount, 2))}.""")

# Output:
# Welcome to the tip calculator!
# What was the total bill? $225
# What percentage tip would you like to give? 10 12 15 15
# How many people to split the bill? 6
# 1.15
# 258.75
# 43.12
#
# The Bill amount is 225.0, you gave the tip of 15%, the total tip was 1.15,
#       The Total Bill amount is 258.75, and each person has to pay 43.12.
# Process finished with exit code 0

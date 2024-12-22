import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

listForHandSigns = [rock, paper, scissors]

# print(listForHandSigns[1])

# choosing either Rock, Paper or Scissors in my_choice
my_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

# Computer is choosing either Rock, Paper or Scissors from computers_choice
computers_choice = random.randint(0, 2)

print(f"You have chosen: {listForHandSigns[my_choice]}\n"
      f"Computer has chosen: {listForHandSigns[computers_choice]}")

# [rock, paper, scissors]
win_or_loose = ["You Win!", "You Lose!"]
if my_choice == computers_choice:
    print("\nits a draw")
elif my_choice != computers_choice:
    if my_choice == listForHandSigns[0] and computers_choice == listForHandSigns[1]:
        print(f"\n{win_or_loose[1]}")
    elif my_choice == listForHandSigns[0] and computers_choice == listForHandSigns[2]:
        print(f"\n{win_or_loose[0]}")
    elif my_choice == listForHandSigns[1] and computers_choice == listForHandSigns[0]:
        print(f"\n{win_or_loose[0]}")
    elif my_choice == listForHandSigns[1] and computers_choice == listForHandSigns[2]:
        print(f"\n{win_or_loose[1]}")
    elif my_choice == listForHandSigns[2] and computers_choice == listForHandSigns[0]:
        print(f"\n{win_or_loose[1]}")
    elif my_choice == listForHandSigns[2] and computers_choice == listForHandSigns[1]:
        print(f"\n{win_or_loose[0]}")
else:
    print("Out of Scope. You Loose!!!!!")

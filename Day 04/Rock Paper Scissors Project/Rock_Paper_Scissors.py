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
if my_choice < 0 or my_choice >= len(listForHandSigns):
    print("You typed an invalid number, you Lose!")
else:
    # Computer is choosing either Rock, Paper, or Scissors
    # Computer is choosing either Rock, Paper or Scissors from computers_choice
    computers_choice = random.randint(0, 2)

    print(f"You have chosen: {listForHandSigns[my_choice]}\n"
          f"Computer has chosen: {listForHandSigns[computers_choice]}")

    # [rock, paper, scissors]
    win_or_loose = ["You Win!", "You Lose!"]
    if my_choice == computers_choice:
        print("\nits a draw")
    elif (my_choice == 0 and computers_choice == 2) or \
            (my_choice == 1 and computers_choice == 0) or \
            (my_choice == 2 and computers_choice == 1):
        print("\nYou Win!!!")
    else:
        print("You Loose!!!!!")

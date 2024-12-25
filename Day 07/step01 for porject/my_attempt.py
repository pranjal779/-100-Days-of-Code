import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.

chosen_word = random.choice(word_list)

print(chosen_word)


usr_guess = input("Enter a letter to guess the word: ")
guess = usr_guess.lower()
print(f"\nUser's guess is: {guess}")

for chword in chosen_word:
    if chword == guess:
        print(f"Right: {chword}")
    else:
        print(f"Wrong: {chword}")


print(type(usr_guess))
print(type(guess))
print(type(chosen_word))

# Output:

# baboon
# Enter a letter to guess the word: b

# User's guess is: b
# Right: b
# Wrong: a
# Right: b
# Wrong: o
# Wrong: o
# Wrong: n
# <class 'str'>
# <class 'str'>
# <class 'str'>

# Process finished with exit code 0


# ------
# if guess in randomlyChosenWord:
#     print(f"{guess}: Right")
# else:
#     print(f"{guess}: wrong")

# baboon
# Enter a letter to guess the word: a
# a: Right
#
# Process finished with exit code 0
# aardvark
# Enter a letter to guess the word: h
# h: wrong
#
# Process finished with exit code 0
#
# baboon
# Enter a letter to guess the word: b
# Right
# wrong
#
# Process finished with exit code 0

# -----------

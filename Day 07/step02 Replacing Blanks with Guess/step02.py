import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word

words_length = len(chosen_word)
placeholder = ""
for position in range(words_length):
    placeholder += "_"
print(placeholder)
guess = input("Guess a letter: ").lower()


# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.

display = ""

for eachletter in chosen_word:
    if guess == chosen_word:
        display += guess
    else:
        display += "_"

    print(display)

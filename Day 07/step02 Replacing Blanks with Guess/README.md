# Step 2 - Replacing Blanks with Guesses

## TODO-1

Create an empty String called placeholder.
For each letter in the chosen*word, add a * to placeholder.
So if the chosen*word was "apple", placeholder should be * \_ \_ \_ _ with 5 "_" representing each letter to guess.
Print out hint.

## Hint 1

Remember you can use the range() function inside a loop to carry out an action for a particular number of times.

## TODO-2

Create an empty string called "display".
Loop through each letter in the chosen*word
If the letter at that position matches guess then reveal that letter in the display at that position.
e.g. If the user guessed "p" and the chosen word was "apple", then display should be * p p \_ _.
Print display and you should see the guessed letter in the correct position.
But every letter that is not a match is represented with a "_".

## Hint 2

Remember that the for loop will go through each letter in the chosen*word in order. You can use that fact to create a new string, appending the letter or an "*".

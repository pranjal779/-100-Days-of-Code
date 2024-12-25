# Step03 Checking if the Player has Won

## TODO-1

Use a while loop to let the user guess again.
The loop should only stop once the user has guessed all the letters in the chosen\*word.
At that point display has no more blanks ("\_"). Then you can tell the user they've won.

### Hint 1

You can use the in keyword to check if a String or List contains a particular item.
e.g. Google: check if a letter is present in a string python

## TODO-2

Update the for loop so that previous guesses are added to the display String.
At the moment, when the user makes a new guess, the previous guess gets replaced by a "\_". We need to fix that by updating the for loop.

### Hint 2

Think about how you can store the matched letters and use an elif to check if a letter has been matched before.

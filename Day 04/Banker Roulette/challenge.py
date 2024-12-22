import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# solution 2
friend_that_will_pay = random.choice(friends)
print(f"The Friend that will pay for bill at random: {friend_that_will_pay}")


# Solution 2
random_index = random.randint(0, 4)
print(f"Random friend who will pay by friends[random_index] way: {
      friends[random_index]}")

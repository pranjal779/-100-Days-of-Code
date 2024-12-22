import random
# import my_module

# random_integer = random.randint(1,10)
#
# print(random_integer)

# print(my_module.my_favorite_number)

random_number_0_to_1 = random.random()
print(random_number_0_to_1) # Return the next random floating-point number in the range 0.0 <= X < 1.0
# example output: 0.2546058470310517


# This example is a semi-open range
random_number_0_to_1_multiplied_by10 = random.random() * 10
print(random_number_0_to_1_multiplied_by10)
    # Return the random floating-point number in the range of 0.0 <= X <= 10.00, excluding 10.00
    # Example Output: 7.1710474358808245, 1.4053767456095179, 3.4870355604425827


# using random.uniform(a, b)
# Return a random floating-point number N such that
# a <= N <= b for a <= b and b <= N <= a for b < a.
#
# The end-point value b may or may not be included in the range depending on floating-point
# rounding in the expression a + (b-a) * random().
random_floating_generator = random.uniform(1, 10)
print(random_floating_generator)
# example Output:7.223755516600304

heads_or_tail = random.randint(1,2)
if heads_or_tail == 1:
    print("Heads")
else:
    print("Tails")

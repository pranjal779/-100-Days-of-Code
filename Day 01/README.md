Printing, Commenting, Debugging, String Manipulation and Variables

```py
print("Hello " + input("what is your name?:") + "!")
```

```py
input("What is your name?")

name = input("Name: ")
print(name)

len_name = len(name)
print(len_name)


print(len(input("What is your Name?:")))

sername = input("your name?")
length = len(username)
print(length)
```

What is your name?sid
Name: samkgh
samkgh
6
What is your Name?:yusoko
6

# Exercise 5 Variables

```py
glass1 = "milk"
glass2 = "juice"

glass2, glass1 = glass1, glass2
print(glass1)
print(glass2)
```

Output:
juice
milk

```py
glass1 = "milk"
glass2 = "juice"

glass3 = glass1
glass1 = glass2
glass2 = glass3
print(glass1, glass2)
```

Test Cases
Failed: 0, Passed: 2 of 2 tests
test_glass1
test_glass2
Your code passed this test

# Exercise 6:

```py
print("Hi How are you? Ready to Rock!")
city_name = input("Tell the name of the city you grew up in?:\n ")
pets_name = input("Your Pet's name?:\n ")
print(city_name + " " + pets_name)
```

Hi How are you? Ready to Rock!
Tell the name of the city you grew up in?:
new york
Your Pet's name?:
bull
new york bull

Click Run to run the final project you will build.
Welcome to the Band Name Generator.
What's the name of the city you grew up in?
nyc
What's your pet's name?
bulkl
Your band name could be nyc bulkl

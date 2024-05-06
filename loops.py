# Loops in Python allow you to execute a block of code repeatedly.
# There are two main types of loops in Python: for loops and while loops.

# 1. For Loop:
#    - The for loop is used to iterate over a sequence (such as a list, tuple, dictionary, or string) or any iterable object.
#    - Syntax:
#      for item in iterable:
#          # Code to execute for each item in the iterable
#    - Example:
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# 2. While Loop:
#    - The while loop is used to repeatedly execute a block of code as long as a specified condition is true.
#    - Syntax:
#      while condition:
#          # Code to execute as long as the condition is true
#    - Example:
i = 1
while i <= 5:
    print(i)
    i += 1
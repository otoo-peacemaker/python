# Conditionals in Python allow you to make decisions in your code based on whether certain conditions are true or false. They are typically implemented using if, elif (else if), and else statements. Here's a brief overview of conditionals in Python:

# 1. if statement:
#    - The if statement is used to execute a block of code only if a specified condition is true.
#    - Syntax:
#      if condition:
#          # Code to execute if condition is true

x = 10
if x > 5:
    print("x is greater than 5")

# 2. if-else statement:
#    - The if-else statement allows you to execute one block of code if the condition is true and another block if the condition is false.
#    - Syntax:
#      ```python
#      if condition:
#          # Code to execute if condition is true
#      else:
#          # Code to execute if condition is false
#    - Example:
x = 3
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")

# 3. elif statement:
#    - The elif statement is used to add additional conditions to an if-else statement.
#    - Syntax:
#      ```python
#      if condition1:
#          # Code to execute if condition1 is true
#      elif condition2:
#          # Code to execute if condition2 is true
#      else:
#          # Code to execute if none of the conditions are true
#    Example:
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")
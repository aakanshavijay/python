# a variable allows python to store and reuse information.

name = "Rahul"
age = 19
percentage = 87.5
is_enrolled = True

#unlike other programming languages, python does not require you to declare the type of variable. 
# Python automatically assigns the type based on the value assigned to the variable.

value = 10
value = "Hello"

#both are valid, as python is dynamically typed. The type of the variable can change based on the value assigned to it.

#DATA TYPES

#fundamental data types in python include:
#1. int - for whole numbers
#2. float - for decimal numbers
#3. str - for text 
#4. bool - for boolean values (True or False)

#Type of a variable can be checked using the type() function.
print(type("10"))
print(type(10))

#Type conversion is the process of converting a variable from one data type to another. 
# Python provides built-in functions for type conversion.

age_text = "19"
age = int(age_text)

price_text = "99.50"
price = float(price_text)

score = 85
score_text = str(score)

#eg
first = input("Enter first number: ") #requires int, to actually perform addition
second = input("Enter second number: ")

print(first + second)
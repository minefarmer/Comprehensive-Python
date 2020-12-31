"""
PYTHON IDENTITY OPERATORS
They are used to compare if objects are the same.

Operator    Description
is          Returns True if of same object.
is not      Returns True if not same object.
"""


fruits = ["grapes", "berries"]
my_fruits = ["grapes", "berries"]
fav_fruits = fruits
print(fruits is fav_fruits)  # True

print(fruits is my_fruits)  # False   ### because they are not the same objects

print("apples" not in fruits)



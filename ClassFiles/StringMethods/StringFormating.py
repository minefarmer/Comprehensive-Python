'''                 STRING Formating
    Useing f -string.
F-string is a string literal that is prefixed with a letter f.
The f string contains expressions which are inside curly braces, so the expressions for the f string are placed inside curly braces, which are then replaced by the actual value.
So the curly braces are just a holding container where the actual values will be represented.
The f string is known as an expression that is evaluated at runtime and then formatted.
Runtime basically means when the code is run or executed.
When the code runs, the f-string kicks in and then formats the value.
'''

name = "bluelime"
age = 4
profession = "developer"
# print(f"Hello, {name}, You are {age} years old .")

# print(f"{7 + 7}")

# print(f"{name.upper()} is 247 online learning.")  # BLUELIME is 247 online learning.




'''             Multiline f- string

'''

message = (
    f"Hi {name} . "
    f" You are a {profession}. "
    f" You have been teaching online for {age} years."
)
# print(message)  # Hi bluelime .  You are a developer.  You have been teaching online for 4 years.




'''             Quotations and f- strings

'''

car = {'brand': 'Range Rover', 'model': 'HSE'}
print(f" the car I like is {car['brand']} sports {car['model']}")

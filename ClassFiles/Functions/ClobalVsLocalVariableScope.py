'''                  Global and Local Variable Scopes
Variables defined inside a function body have a local scope.
Variables defined outside a function have a global scope.
Global variables can be accessed anywhere in your python file.
Localvariables can only be accesses inside the function it belongs to.
I can use the global keyword inside a function definition to make the value of a local variable global.



'''
# x = 10  # global variable

# def my_number(x):
#     print(x)  # 10
#     x = 7  #local variable
#     print("My fav number is ", x)

# my_number(x)  # My fav number is  7

# print(x)  # 10    ## x from line 11








# How to change the value of the global variable

x = 10  # global variable

def my_number():
    global x  # By using keyword global here, the x on line 36 changed the global value to 7
    print(x)  # 10
    x = 7  #changed global variable
    print("My fav number is ", x)

my_number()  # My fav number is  7

print(x)  # 7    ## global variable x  after I have changed the global variable on line 36

'''                     Python Decorators
Decorators are used to add new functionality to existung objects like functions, methods and classes without modifying it's structor.
Decorators are usually called before the defination of the object (Function,Method,Class) we want to decorate.
They can be represented by @ followed by name of the decorated object,

More on decorators:
        https://www.python.org/dev/peps/pep-0318/

converting a sentence to uppercase.
Not Working ***********************************************************************************
'''
# def my_decorator(function) :
#     def wapper():
#         myfunc = function()
#         convert_uppercase = myfunc.upper()
#         return convert_uppercase
#     return wrapper
# @my_decorator
# def say_hello():
#     return "hello world"
# # decorate = my_decorator(say_hello)
# print(say_hello())

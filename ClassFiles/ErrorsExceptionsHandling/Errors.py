'''                 Handling Exceptions (Errors)








'''
# print(x)  # Traceback (most recent call last):
        # File "/home/rich/Desktop/CarlsHub/Comprehensive-Python/ClassFiles/ErrorsExceptionsHandling/Errors.py", line 11, in <module>
        #     print(x)
        # NameError: name 'x' is not defined
        

x = 20

try:
    print(x)  # 20
except:
    print("Variable is not defined.")  # Variable is not defined.
else:
    print("Hello")  # Hello
finally:
    print("You may get an error if no variable is specified")  # You may get an error if no variable is specified
    

    
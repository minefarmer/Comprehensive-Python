'''                 Nesting Functions Accessing Variable Scope
Python allows a nested function to access the outer scope of the enclosing function.
This consept is referred to as closure.

'''

def display_message(message):
    "hello"
    def message_sender():
        "nested function"
        print(message)
    message_sender()

display_message("hello world")  # hello world

'''                 VarArgs Parameter
Lets me define variable number of arguments for a function.
They are identified by using the asterisk symbol. *

Note: When the asterisks parameter has just one asterisk, all the positional arguments from that point to the end are collected as a tuple.
Note: When the argument has two asterisks, all the keyword arguments from that point to the end are allocated to a dictionary.


                        Tuple     Dictionary
'''
def total_numbers(a=7, *numbers,**phonebook):
    print('My fav number is ', a)  # My fav number is  7

    for num in numbers:
        print('num', num)  # num 1
                            # num 2
                            # num 3

    for name,phone_number in phonebook.items() :
        print('name', phone_number)  # name 2222
                                    # name 4444
                                    # name 5555

total_numbers(7,1,2,3,Jane=2222,John=4444,Angela=5555)
# When the function is called, the names supplied will be assigned a phone number.
'''                     Python DocStrings
Allows me to display code documentation when code executes.
They are accessed by using double underscore with attribute name.
They are defined using three single quotes and some text.





'''
def add_numbers(d,e):
    '''Adding two numbers
    :param d:
    :param e:
    :return:'''
    print(d + e)


add_numbers(8, 4)   # 12

print(add_numbers.__doc__)  # Adding two numbers
                            # :param d:
                            # :param e:
                            # :return:

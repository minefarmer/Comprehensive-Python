'''             KEYWORD ARGUMENTS
Allows me to specify what parameters to use from a list of parameters.
I do not need to worry about the order of the arguments.
Allow me to give values only to parameters I want to provided the other parameters have default argument values.





'''
def more_num(a,b=7,c=10):
    print("a is ",a, "and b is ",b, "While c is ",c) # a does not have a default value. b and c have a default argument value.
more_num(3,7)  # a is  3 and b is  7 While c is  10
more_num(23,c=17)  # a is  23 and b is  7 While c is  17
more_num(c=40,a=90)  # a is  90 and b is  7 While c is  40

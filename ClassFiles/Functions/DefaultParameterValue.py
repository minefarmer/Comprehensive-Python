'''             DEFAULT PARAMETER VALUE
This is the value a function uses when called without passing it a value.
Only parameters at the end of a parameter list can have a default value as Values are assgned by position.
    def greeting(a, b=7):  # correct way  

'''
def student_names(names="Bluelime"):
    print("Hello " + names)

student_names()  # Hello Bluelime
student_names("Sam")  # Hello Sam
student_names("John")  # Hello John
student_names("Jane")  # Hello Jane


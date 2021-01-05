'''                 Polymorphism : Part 1
Polymorphism basically means the ability to take or have multiple or various forms.
Polymorphim means the ability to take or have various forms.

                    Polymorphism: Part 2   30
Creating a polymorphic class method.   38












                    Polymorphism : Part 1
'''
print(len("Hello World!"))  # 12
print(len([20,40,80]))  # 3







                    # Polymorphism: Part 2
def addNumbers(a,b,c=1):
    return a + b + c

print(addNumbers(8,9))  # 18   ## What I am doing here is passing arguments for the function parameters,
print(addNumbers(8,9,4))  # 21   ## Here I changed the default value of c.


class UK():
    def capital_city(self):
        print("London is the capital of UK")

    def language(self):
        print("English is the primary language ")


class Spain():
    def capital_city(self):
        print("Madrid is the capital of Spain")

    def language(self):
        print("Spanish is the primary language ")



queen = UK()  # Instantiation of the class UK
queen.capital_city()  # This method is now attached to the instance of the class called UK.

zara = Spain()
zara.capital_city()

for country in (queen,zara):
    country.capital_city()
    country.language()  # London is the capital of UK  ## created by looping through the for loop by accessing the print classes 
                        # Madrid is the capital of Spain
                        # London is the capital of UK
                        # English is the primary language
                        # Madrid is the capital of Spain
                        # Spanish is the primary language


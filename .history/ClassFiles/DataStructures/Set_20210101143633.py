'''                 SETS
A set is a collection of values.
Values in a set are not ordered.
Values in a set are not indexed.
How to create a Set with a constructor()  # 28
Counting Values in a Set.  # 36
Built-in Set methods  # 39
Methods     Description
add()       Adds an element to a set.
Update()    Adds multiple elements in a set









'''
fruits = {"grapes", "apples", "berries"}
for x in fruits:
    print(x)  # apples
            # grapes
            # berries


# animals = set(("lion", "tiger","bear"))  # without a constructor
animals = (("lion", "tiger","bear"))  # using a constructor function
for y in animals:
    print(y)  # lion
            # tiger
            # bear


print(len(animals))  # 3




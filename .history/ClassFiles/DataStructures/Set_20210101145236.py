'''                 SETS
A set is a collection of values.
Values in a set are not ordered.
Values in a set are not indexed.
How to create a Set with a constructor()  # 28
Counting Values in a Set.  # 35
Built-in Set methods
Methods     Description
add()       Adds an element to a set.  # 37
Update()    Adds multiple elements in a set.  # 40
clear()     Removes all elements in a set.
discard()   Removes a specific element or item.
remove()    Removes a specific item from the set.  # 43
del()       Deletes the set.





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

fruits.add("oranges")
print(fruits)  # {'apples', 'oranges', 'grapes', 'berries'}

fruits.update(["mango", "kiwi"])
print(fruits)  # {'grapes', 'apples', 'berries', 'mango', 'oranges', 'kiwi'}

fruits.remove("kiwi")
print(f)

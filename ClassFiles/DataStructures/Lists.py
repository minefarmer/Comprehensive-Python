'''                 List
Accessing Elements of a List  32








A list is a collection of data which can be of mixed type.
Items in a list are ordered by their index and changeable.
Lists are created with square brackets. []
Items in a list can be accessed by their index,
Each item in a list is separated by a comma.

I can also create a list using a constructor, which is a function used to create objects.
    animals = list(("bear","lion", "tiger"]
'''

animals = ["bear", "lion","tiger", "panda", "elephant"]
# for x in animals:
#     print(x)  # bear
#             # lion
#             # tiger
#             # panda
#             # elephant
# print(animals)  # ['bear', 'lion', 'tiger', 'panda', 'elephant']



'''                 Accessing Elements of a List
A list can be accessed using their index or position in the list.

'''

print(animals[0])  # bear
print(animals[-1])  # elephant
print(animals[1:])  # ['lion', 'tiger', 'panda', 'elephant']
print(animals[1:3])  # ['lion', 'tiger']

animals[0] = "dog"
print(animals[0])  # dog

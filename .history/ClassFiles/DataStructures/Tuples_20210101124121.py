'''                 Tupels
A Tuple is a list that can not be changed. (immutable)
Can be created using parenthesis. () and with a constructor
Elements in a tuple can be accessed by their index.
For loop use in tuple  # 21
Accessing elements in a tuple.  # 27
Creating a Tuple with a Tuple constructor. Tuples are immutable.  # 30












'''
fruits = ("grapes", "apples", "berries")
for x in fruits:
    print(x)  # grapes
            # apples
            # berries

print(fruits[2])  # berries


animals = tuple(("lion", "tiger", "bear"))
print(animals)  # ('lion', 'tiger', 'bear')
print(animals[2])  # bear
print(len(animals))  # 3
# animals.add("dog")  # Traceback (most recent call last):
                    # File "c:\Users\pgold\CarlsHub\Comprehensive-Python\ClassFiles\DataStructures\Tuples.py", line 34, in <module>
                    #     animals.add("dog")
                    # AttributeError: 'tuple' object has no attribute 'add'
animals[0] = "cheetah"  # 
'''                 STRING METHODS
len() is used to find the length of a string.

index()  returns position of a string or charactor. The position of the first letter of a word

capitalize()

upper()
lower()

islower()
isupper()

find()  # used to find the first index occurrence of a string or charactor.

count()  # Counts the occurrence of a string or character.

split()  # Used to split a string into a list.

\n  # Used to split characters or words into different or separate lines.

Concatenation +  # Adds strings or characters together.

replace()  # Replaces strings or characters.  
           # Takes two parameters. What to replace and what it with.
'''

g = "hello world."

print(len(g))  # 12

print(g.index("world"))

print(g.capitalize())  # Hello world.

print(g.upper())  # HELLO WORLD.

print(g.islower())  # True.

print(g.find("world"))  # 6

print(g.count("l"))  # 3

print(g.split())  # ['hello', 'world.']

print("show me\n d money")  # show me
                            #  d money

print(g + " I Hope u r doing ok.")  # hello world. I Hope u r doing ok.

print(g.replace("world", "people"))  # hello people.

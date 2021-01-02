'''                 List Methods
extend()    Used to append or join list contents.  # 17
append()    Adds an item to the end of the list.   # 20
sort()      Orders list items. Ascending or Descending.  # 23
sort(reverse=True)  # 26
count()     Counts the occurrence of a list item.  # 29
index()     Returns the index position of a list item.  # 31
insert()    Adds a new item to the list.  # 33
            Takes two parameters: Index and item
pop()       Removes the last item from the list.  # 36


''' 
fruits = ["berries", "apples", "grapes", "oranges"]
vegetables = ["kale", "broccoli", "lettuce"]

fruits.extend(vegetables)
print(fruits)  # ['berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettuce']

vegetables.append("bean")
print(vegetables)  # ['kale', 'broccoli', 'lettuce', 'bean']

vegetables.sort()
print(vegetables)  # ['bean', 'broccoli', 'kale', 'lettuce']

vegetables.sort(reverse=True)
print(vegetables)  # ['lettuce', 'kale', 'broccoli', 'bean']

print(fruits.count("berries"))  # 1

print(fruits.index("grapes"))  # 2

fruits.insert(0, "banana")
print(fruits)  # ['banana', 'berries', 'apples', 'grapes', 'oranges', 'kale', 'broccoli', 'lettuce']

fruits

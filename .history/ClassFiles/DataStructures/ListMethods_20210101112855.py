'''                 List Methods
extend()    Used to append or join list contents.  # 17
append()    Adds an item to the end of the list.   # 21
sort()      Orders list items. Ascending or Descending.  # 26
count()      Counts the occurrence of a list item.  # 32






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

print(fruits.index)

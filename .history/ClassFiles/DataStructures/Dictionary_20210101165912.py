'''                 Dictionary
A dictionary is a collection of key value pairs.
The values can be changed (mutable)
The values have unique keys.
Using the constructor method  # 29
                Built-in dictionary Methods
Method      Description
get()       Returns the value of a specific key.  # 37
Update()    Inserts a specified key:value pair.  # 39
clear()     Removes all key:value pairs in dictionary
keys()      Returns a list of dictionary keys.  # 42
values()    Returns a list of dictionary values.  # 45
del()       Deletes the dictionary
Count key:value pairs  # 32
Change value of a key  # 34




'''
mycar = {
    "brand": "Range Rover Sports",
    "model": "HSE",
    "year": 2017
}
print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2017}


mygreens = dict(fruit="green apples", vegetables="kale")
print(mygreens)  # {'fruit': 'green apples', 'vegetables': 'kale'}

print(len(mycar))  # 3

mycar["year"] = 2019
print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2019}

print(mycar.get("year"))  # 2019

mycar.update({"color": "silver"})
print(mycar)  # {'brand': 'Range Rover Sports', 'model': 'HSE', 'year': 2019, 'color': 'silver'}

b = mycar.keys()
print(b) # dict_keys(['brand', 'model', 'year', 'color'])

b = 

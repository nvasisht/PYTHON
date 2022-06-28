# Can access the items of the dictionary by referring to
#key name, inside a square brackets '[]'

# Give the value of the 'model' key:

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year": 1964
}
x = thisdict["model"]
# Output ---- Mustang


# There is also a method called get() that will give you the same result.

# get the value of the "model" key:
x = thisdict.get("model")
# Output ---- Mustang


# GET KEYS
# The keys () will return a list of all the keys in the dictionary 

# Get a list of keys:
x = thisdict.keys()
# The list of the keys is a view of the dictionary, meaning that any changes 
# done to the dictionary will be reflected in the keys list.

# Add a new item to the original dictionary,
#  and see that the keys list gets updated as well:

car = {
    'brand':'Ford',
    'model': 'Mustang',
    'year': 1964
}
x = car.keys() # before the change
print(x) # dict_keys(['brand', 'model', 'year'])

car["color"]= 'white'
print(x) # After the change
# dict_keys(['brand', 'model', 'year', 'color'])


# GET VALUES ()

# The values () method will return a list of all the values in the dictionary 

# Get a list of values()

x = thisdict.values()
# The list of the values is a view of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the values list.

# Make a change in the original dictionary,
#  and see that the values list gets updated as well:


car = {
    'brand': 'Ford',
    'model': 'Mustang',
    'year':1964
}
x = car.values()
print (x) # before the change
# dict_values(['Ford', 'Mustang', 1964])

car['year'] = 2022

print(x) # after the change
# dict_values(['Ford', 'Mustang', 2022])


# Add a new item to the original dictionary, 
# and see that the values list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["color"] = "red"

print(x) #after the change



# GET ITEMS 

# The items () method will return each item in a dictionary as tuples in a list

# Get a list of the key:value pairs
x = thisdict.items()

# The returned list is a view of the items of the dictionary, 
# meaning that any changes done to the dictionary will be reflected in the items list.

# Make a change in the original dictionary, 
# and see that the items list gets updated as well:

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

car["year"] = 2020

print(x) #after the change
#dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])


# Add the new item to the orginal dictionary
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["color"] = "red"

print(x) #after the change
# dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])



# Check if Key Exists

# To determine if a specified key is present in a dictionary use the in keyword:

# Check if "model" is present in the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes the model is exsiting")


# If not exixting 

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "color" in thisdict:
    print("No, the color does not exist in the dictionary")


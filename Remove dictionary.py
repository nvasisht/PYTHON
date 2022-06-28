
# Removing Items 

# There are several methods to remove items from a dictionary:

# The ---pop()---method removes the item with the --specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") # model is a specific item 
print(thisdict)

# The ---popitem()-- method removes the last inserted item

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() # Automatically removes the last item
print(thisdict)

# The --del-- keyword removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["brand"]
print(thisdict)


# The --del--- keyword can also delete the dictionary completely:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict)
# Output --- thisdict' is not defined


# The-- clear()--- method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
# Output ---- {}

# APPEND ITEMS 

#To add an item to the end of the list use append()


import this


thislist =["apple", "banana", "watermelon"]
thislist.append("oranges")
print(thislist)

# Insert Items
#To insert a list item at a specified index, use the insert() method.

thislist =["apple", "banana", "watermelon"]
thislist.insert(0, "oranges")
print(thislist)
print(len(thislist)) # displays 4 items


#Extend List 
# To append elements from another different list to the current list use extend()

# Add elements of tropical to thislist

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


#Add Any Iterable 
# The extend () method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries... etc)

# Add tuple :
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
print(len(thislist))
#  Python Sets

# Sets are used to store multiple items in a single variable.
# Set is one of 4 built-in data types in Python used
#  to store collections of data, 
# the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

#  Set items are unchangeable, but you can remove items and add new items 

# Sets are written in curly brackets {}

# Sets are unordered.

# Create a set:

set = {"apple", "banana", "cherry"}
print(set) 
#Output ---- {'banana', 'apple', 'cherry'}



# Unordered 

# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you 
# use them, and cannot be referred to by index or key.



# Unchangeable

# Set items are unchangeable, meaning that
#  we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items,
#  but you can remove items and add new items.


# Duplicates Not Allowed

# Sets cannot have two items with the same value.

# Duplicates values will be ignored:

set = {"apple", "melon","cherry", "apple"}
print(set) 
# Output --- {'apple', 'melon', 'cherry'} the last 'apple' is ignored.


# Get the length of Set 

# To determine how many items a set has, use --len()-- 

set = {"banana", "orange", "melon", "grape", "strawberry"}
print(len(set))
# Has 5 items 


# Set items --- Data types 

# Set items can be of any data type 
# String, int and boolean

set1 = {"glass", "mug", "cup"}
set2 = {1,2,3}
set3 = {True, False, True}
print(set1)
print(set2)
print(set3)


# A set can contain different data types within the set elements

set1 = {"abc", 50, True, 90, "Mug"}
print(set1)



# Type ()

#From Python's perspective, 
# sets are defined as objects with the data type 'set':
# <class 'set'>

#What is the data type of a set?
set = {"glass", "Mug", "Cup"}
print(type(set))
#Output ---- <class 'set'>

# The set() Constructor

# It is also possible to use the set() constructor to make a set.

# Using the set() constructor to make a set:

thisset= set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
# Output --- {'cherry', 'apple', 'banana'}
# Note: the set list is unordered, so the result will display the items in a random order.

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable.  Allows duplicate members
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.



#Lists are used to store muliple items in a single variable 

#Lists are one of the four bulit-in data types in Python used to store 
# a collections of data, the others are Tuples, set and dictionary all with different qualities and usage.

thislist = ["apples", "banana", "cherry"]
print(thislist)


# List Items 

# Are ordered, changeable and allow duplicate values
# List items are indexed, the first item has [0], the second item has index [1]


# ORDERED
# lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list

#Changeable
#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

#Allow Duplicates
#Since lists are indexed, lists can have items with the same value

thislist = ["apple", "cherries", "apple", "cherries"]
print(thislist)

#List Length
#To determine how many items a list has use --len()--

thislist = ["apple", "banana", "orange", "cherries"]
print(len(thislist)) # displays 4 items

#List Items  ---- ANY Data Types
#String, int and boolean
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

# A list can contail different data types 
list1 = ['abc', 55, True, 'Female']
print(list1)

#TYPE()
#Lists are defined as objects with the data type 'list' <class 'list'>

mylist = ['apple', 'banana', 'cherry']
print(type(mylist)) #list is the datatype


#The list() Constructor
# Use list() constructor when creating new lists

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


# Python Collections (Arrays)
# here are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

# *Set items are unchangeable, but you can remove and/or add items whenever you like.
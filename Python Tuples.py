# Tuple

#Tuple are used to store multiple items in as single variable.

#Tuple is one of 4 built-in data types:
#  in Python used to store collections of data,
#  the other 3 are List, Set, and Dictionary, all with different qualities and usage.

#Tuples is a collection which is ordered and unchangeable.

#Tuples are write with round brackets ()

import this


thistuple = ("apple", "mango", "banana")
print(thistuple)


#Tuple Items 

#Tuple items are:
#  ordered ----  the items have a defined order, and that order will not change.
# unchangeable --- we cannot change, add or remove items after the tuple has been created.
# allow duplicate values --- tuples are indexed, they can have items with the same value.

#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

#Tuples allow duplicates values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#Output --- ('apple', 'banana', 'cherry', 'apple', 'cherry')

#Tuple Length 
# To determine how many items a tuple has use --len()--

thistuple = ("mango", "pineapple", "watermelon")
print(len(thistuple))

thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #Indicating a specific index within the element


# Create Tuple with One Item 
# To create only one item, you have to add a comma after the item,
#otherwise python will not recognize it as a tuple 

thistuple = ("cherry",) #type is tuple
print(type(thistuple))


#Not a tuple
thistuple = ("cherry") #tupe is string
print(type(thistuple))

#Tuple Items ---- Data Types

#Tuple items can be of any data types: str, int & bool

tuple1 = ("apple", "cherry", "mango")
tuple2 = (1,2,3,4,5)
tuple3 = (True, False, True)

print(tuple1)
print(tuple2)
print(tuple3)

tuple1 = ("abc", 34, True, 40, "male")

print(tuple1)

# The type()

#From Python's perspective, tuples are defined as objects with the data type 'tuple':
# <class 'tuple'>

#What is the data type of a tuple?
mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) #<class 'tuple'>


# The tuple () Constructor 

# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)



# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

#List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


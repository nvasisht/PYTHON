# Access Tuple Items 

# You can access tuples items by referring to the index numbers, inside square brackets.

#Print the second item in the tuple:

# The first item has index 0

tuple = ("mango", "watermelon", "pineapple", "cherry")
print(tuple[2])

#Neagtive Indexing 

# Negative indexing means start from the end.
# Negative index start from -1
# -1 refers to the last item, -2 refers to the second last item and so on.

tuple = ("mango", "watermelon", "pineapple", "cherry")
print(tuple[-4])


# Range of Indexes

# You can specify a range of indexes
#  by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new tuple
#  with the specified items.

#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Note: The search will start at index 2 
# (included) and end at index 5 (not included).

# This example returns the items from the beginning to, but NOT included, "kiwi":

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
# Include "apple", "banana", "cherry", "orange"

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[4:])
# Include "Kiwi", "melon", "mango"

# Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the tuple:
#returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) 
# Includes "orange", "kiwi", "melon" but not "mango"


# Check if items exists
#To determine if a specified item is present in a tuple use the  -- in -- keyword:

# Check if apple is present in the tuple:

tuple = ("mango", "melon", "apple", "cherry")
if "apple" in tuple:
    print("Yes, 'apple' is in the fruits tuple")

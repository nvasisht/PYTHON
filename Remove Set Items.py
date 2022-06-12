# Remove Item 

# To remove an item in a set, 
# use the ---remove()---, or the ---discard()--- method.

import this


thisset = {"apple", "cherry", "banana", "orange"}
thisset.remove("banana")
print(thisset)
# Output --- {'cherry', 'apple', 'orange'}

# Note: If the item to remove does not exist, remove() will raise an error.


# Remove "banana" by using the discard() method:

thisset = {"banana", "cherry", "mango", "apple"}
thisset.discard("banana")
print(thisset)

# Note: If the item to remove does not exist, discard() will NOT raise an error.


# pop ()

# You can also use the--- pop()--- method to remove an item, 
# but this method will remove the last item.--------- 
# Remember that sets are unordered, so you will not know what item that gets removed.

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# Clear ()
# The clear() method empties the set:

thisset = {"banana", "cherry", "mango", "apple"}
thisset.clear()
print(thisset)
# Output --- set()


# Delete ()

# The del keyword will delete the set completely:
fruits = {"banana", "cherry", "mango", "apple"}
del fruits
print(fruits)

# Output --- NameError: name 'fruits' is not defined

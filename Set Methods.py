# Set Methods

# Python has a set of built-in methods that you can use on sets.

# add()	Adds an element to the set

# Add an element to the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

# clear()	Removes all the elements from the set

# Remove all elements from the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
# Output -- set()

# copy()	Returns a copy of the set

# Copy the fruits set:
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)

# difference()	Returns a set containing the difference between two or more sets

# Return a set that contains the items that only exist in set x, and not in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"} # not displayed
z = x.difference(y)
print(z)
#Output ---  { "banana", "cherry"} remove any duplicates

# difference_update()	Removes the items in this set that are also included in another, specified set

# Remove the items that exist in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

# difference() method returns a new set, without the unwanted items
# difference_update() method removes the unwanted items from the original set.

# discard()	Remove the specified item

# Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)

# intersection()	Returns a set, that is the intersection of two other sets

# Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z) 
# Output -- {'apple'}


# intersection_update()	Removes the items in this set that are not present in other, specified set(s)

# Remove the items that is not present in both x and y:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
# Output --- {'apple'}


# isdisjoint()	Returns whether two sets have a intersection or not

# Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
# True --- no duplicates


# issubset()	Returns whether another set contains this set or not

# Return True if all items in set x are present in set y:
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)
# True --- There are duplicates of {'a','b', 'c'}


# issuperset()	Returns whether this set contains another set or not

# Return True if all items set y are present in set x:

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)
# True --- {'a','b','c'}


# pop()	Removes an element from the set

# Remove a random item from the set:
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

# remove()	Removes the specified element

#Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)


# symmetric_difference()	Returns a set with the symmetric differences of two sets

# Return a set that contains all items from both sets, except items that are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
# Output --- {'banana', 'microsoft', 'cherry', 'google'}
# Removes any duplicates


# symmetric_difference_update()	inserts the symmetric differences from this set and another

# Remove the items that are present in both sets, AND insert the items that is not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
# Output --- {'cherry', 'google', 'microsoft', 'banana'}



# union()	Return a set containing the union of sets

#Return a set that contains all items from both sets, duplicates are excluded:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)

# update()	Update the set with the union of this set and others

#Insert the items from set y into set x:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)
# Output --- {'apple', 'banana', 'microsoft', 'cherry', 'google'}

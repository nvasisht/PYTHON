# Join Sets 

# There are several ways to join two or more sets in Python 

# You can use ---union() --- method that returns a new containing all items,
# from both sets or ---update()--- methods that inserts all 
# items from one set to another.

# The --union () returns a new set with all items from both sets:

set1 = {"a","b", "c"}
set2 = {1,2,3}
set3 = set1.union(set2)
print(set3)


# The update () inserts the items in set2 into set1:
set1 = {"a","b", "c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)

# Note: Both union() and update() will exclude any duplicate items.
set1 = {"a","b", "c", "c"}
set2 = {1,2,3}
set1.update(set2)
print(set1)


# Keep ONLY the Duplicates

# The ---intersection_update()--- method keep only 
# the items that are present in both sets:

# Keep the items that exists in both x and y sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# OR
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
y.intersection_update(x)
print(y)

# The ---intersection() method --- will return a new set, that
#only contains he items that are present in both sets.

# Return a set that contains the items that exist in both x & y sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.intersection(y)
print(z)

# Keep ALL, but NOT the Duplicates

# The ---symmetric_difference_update()-- method to keep only
# the elements that are NOT present in both sets

# Keep the items that are not present(non-duplicates) in both sets:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
# Output ---  {'banana', 'google', 'cherry', 'microsoft'}

# The --- symmetric_difference () method-- will return a new set,
# that contains only the elements that are NOT present in both sets
# (non-duplicates)

# Return a set that contains all items from both sets, except items that are present in both:

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z=x.symmetric_difference(y)
print(z)
# Output --- {'microsoft', 'cherry', 'banana', 'google'}
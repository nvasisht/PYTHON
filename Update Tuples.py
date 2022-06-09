# Tuples are unchangeable, meaning that you cannot change, 
# add, or remove items once the tuple is created.

# Change Tuple Values:
# Once a tuple is created, you cannot change its values

# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi" #replacing banana with 'kiwi'
x = tuple(y)
print(x)

# Add Items 
#Use append() to add into the tuple 

#Convert into a list:
#ust like the workaround for changing a tuple, 
# you can convert it into a list, add your item(s),
#  and convert it back into a tuple.

# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)


# Add tuple to a tuple. 
# You are allowed to add tuples to tuples, 
# so if you want to add one item, (or many), 
# create a new tuple with the item(s), and add it to the existing tuple:

# Create a new tuple with the value "orange", and add that tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

#Note: When creating a tuple with only one item, 
# remember to include a comma after the item, 
# otherwise it will not be identified as a tuple.

# Remove Items 

# Note: You cannot remove items in a tuple.

#Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# you can delete the tuple completely:
# the del keyword can delete the tuple completely:

thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) # 'thistuple ' is not defined
 #this will raise an error because the tuple no longer exists

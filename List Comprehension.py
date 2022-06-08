# offers a shorter syntax when you want to create a new list 
# based on the values of an existing list.

# Example:

#Based on a list of fruits,
#  you want a new list, 
# containing only the fruits with the letter "a" in the name.

#Without list comprehension you will have to write a --for--
#statement with a conditional test inside:

fruits = ["apples", "mango", "banana","cherry", "kiwi"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#With the list comprehension you can do all that with one line of code :

fruits = ["apples", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


# THE SYNTAX

# newlist = [expression for item in iterable if condition == True]

# The return value is a new list, leaving the old list unchanged.

# CONDITION
# The condition is like a filter that only accepts the items that valuate to --True--.

# Only Accepts items that are not "apple"
# he condition if x != "apple"  will return --True for all elements other-- than "apple", 
# making the new list contain all fruits except "apple".
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x !="apple"]
print(newlist)



# Conditi0n is optional and can be omitted:
#With no if statement:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits ]
print(newlist)


# Iterable 

# Iterable can be any object, like list, tuple and set

# Use --range()-- to create an iterable

newlist = [x for x in range(10) ]
print(newlist)

# But with a condition:

#Accepts only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]
print(newlist)




# EXPRESSION 

# Expression is the current item in the iteration,
# but it is also the outcome which you can manipulate before its ends up like a list item in a new list:

#set values in the new list to upper case:

fruits = ["apples", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

# Lower case:
fruits = ["APPLES", "BANANA", "CHERRY", "KIWI", "MANGO"]
newlist = [x.lower() for x in fruits]
print(newlist)

# Set outcome to whatever you like:
#Set all values in the new list to 'hello'

fruits = ["apples", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)


# Expression can also contain conditions, not like filter but as a way to manipulate the outcome:

fruits = ["apples", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# "Return the item if it is not banana, if it is banana return orange".




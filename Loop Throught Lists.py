# Loop Throught a List 

# You can loop throught the items by using --for-- loop

#Print all items in the lists, one by one:

import this


thislist = ["apple", "cherry", "banana"]
for x in thislist:
 print(x)


# Loop Throught the Index Numbers
#You can loop throught the lists items by referring to their index number 

# Use the ---range()--- and --len()-- functions to create suitable iterable 

#Print all items by referring their index numbers:

thislist = ["apple", "cherry", "banana"]
for x in range(len(thislist)):
    print(thislist[x])
# The iterable created [0,1,2]


# Using while loop

#Use the len() function to determine the length of the list, then start at 0 
#loop your way through the list items by refering to their indexes.

#Remember to increase the index by 1 after each iteration.

# Print all items, using a ---while loop--- to go through all the index numbers

thislist = ["apple", "cherry", "banana"]
i =0
while i < len(thislist):
 print(thislist[i])
i = i + 1

# Looping using List comprehension

#Offers the shortest syntax for looping throught lists:
# Ashort hand --for-- loop that will print all items in a list:

thislist =["apples", "banana", "Cherry"]
[print(x) for x in thislist]


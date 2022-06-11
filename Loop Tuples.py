# Loop Throught a tuple 

#You can loop through the tuple items by using ---for loop----

#Iterate through the items and print the values 

from socketserver import ThreadingUnixStreamServer


thistuple = ("apple","banana", "cherry")
for x in thistuple:
 print(x)

 #Loop through the index Numbers

 #You can also loop through the tuple items by referring to their index numbers

 # Use the --range() and len()--- to create a suitable iterable

#print all items by referring to their index numbers:

thistuple = ("apple","banana", "cherry")
for i in range(len(thistuple)):
 print(thistuple[i]) #Still no understanding 

 #While Loop

 #You can loop through the items by using --while loop---

#Using ---len()--- to determine the length of the tuple,
# then start at 0 and loop your way through the tuple items by referring to their indexes. 

# Rememeber to increase the index by 1 after iteraction 

# Print all items using --while loop-- to go through all the index numbers:

thistuple = ("cherry", "melon","pineapple")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
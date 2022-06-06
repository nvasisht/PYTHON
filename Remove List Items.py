# Remove List Items 

# To remove any specified item or list use --remove ()-- method.

thislist = ["apple", "watermelon", "cherry"]
thislist.remove("cherry")
print(thislist)
print(len(thislist))

#Remove Specified Index 

# Use --pop ()-- to remove specified index

thislist = ["apple", "watermelon", "cherry"]
thislist.pop(0)
print(thislist)
print(len(thislist))

# OR remove the last item or list

thislist = ["apple", "watermelon", "cherry"]
thislist.pop()
print(thislist)

# Can use --del -- keyword also to remove the specified index 
# del -- means Delete

thislist = ["watermelon", "mango", "banana"]
del thislist[0]
print(thislist)


# Delete the entire list
thislist = ["watermelon", "mango", "banana"]
del thislist
print(thislist) #--- Not available 

# Clear the List

# Empties the list, the list still remains but has no content 

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
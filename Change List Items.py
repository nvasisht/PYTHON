# Change Item Value

#To change the value of a specific item, refer to the index number:
# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "orange"
print(thislist)


# Change a Range of Item Values
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] =["blackcurrant", "watermelon"]
print(thislist)

#NOTE : The length of the list will change when the number of items inserted does not match the number of items replaced.

# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)



# Insert Items 
# To insert a new list item without replacing any existing values use insert() at the specified index

#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "oranges")
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "oranges")
print(thislist)
print(len(thislist)) # displays 4 items
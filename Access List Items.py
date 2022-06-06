# Access Items
#List items are indexed and you can access them by referring to the index number 

acclist = ['apple', 'cherry', 'banana'] # index starts with ( 0 ) 0-apple, 1-cherry, 2-banana
print(acclist[1])

#Range of Indexes

# You can specify a range of indexes by specifying where to start and where to end the range 
# and it will return value will be new list with the specified items.

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) # Return 3,4 and 5
print(thislist[5])
#The search will start at index 2 (included) and end at index 5 (not included).

# By leaving out the start value, the range will start at the first item:
#This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


#By leaving out the end value, the range will go on to the end of the list:
#This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


#Range of Negative Indexes
#Specify negative indexes if you want to start the search from the end of the list:
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


#Check if Item Exists

#To determine if a specified item is present in a list use the in keyword:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")



# Add Items 

# Once a set is created, you can cannot change its items, but you can add new items 

# To add one item to a set use ---add()---

set = {"yellow", "blue", "red"}
set.add("purple")
print(set)


# Add Sets

# To add items from another set into the current set,
#  use the ----update()---- method

fruits = {"apple", "banana", "cherry "}
tropical = {"pineapple", "mango", "papaya"}
fruits.update(tropical)
print(fruits)

# Add Any Iterable

#The object in the update() method does not have to be a set, it can
#  be any iterable object (tuples, lists, dictionaries etc.).

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"] # using a list array

thisset.update(mylist)

print(thisset)
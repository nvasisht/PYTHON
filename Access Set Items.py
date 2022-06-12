# Access Items 

# You cannot access items in a set by referring to an index or a key
#But you can loop through the set items using a for loop, 
# or ask if a specified value is present in a set, by using the in keyword

# Loop through the the set, and print values:

set = {"apple", "banana", "cherry"}
for x in set:
    print(x)


# Check if "banana" is present in the set:

set = {"apple", "banana", "melon"}
print("banana" in set ) # True

# If not
set = {"apple", "banana", "melon"}
print("cherrt" in set ) #False

# Once a set is created, you cannot change its items, but you can add new items.
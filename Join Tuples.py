
# Join Two Tuples

# To join two or more tuples you can use the --(+) operator--

# Join two tuples:

tuple1 = ("kiwi", "mango", "orange")
tuple2 = (1,2,2)
tuple3 = tuple1 + tuple2

print(tuple3)
# Output --- ('kiwi', 'mango', 'orange', 1, 2, 2)


#Multiply Tuples

# If you want to multiply the content of a tuple numbers of timess, you can use the ---*--- operator

#Mulitply the fruits tuple by 2:

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) 
# Output --- ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')
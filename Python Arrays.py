# Python does not have built - in support for arrays,
# but Python lists can be used instead. 


# ARRAYS 

# How to use Lists as Arrays, how to work with arrays  in Python 
# you need to import a library like Numpy Library

# Arrays are used to store mulitple values in one single variable

# Create an array containing car names:

cars = ["Ford", "Volvo", "BMW"]
print(cars)


# What is an Array ?

# An array is a special variable, which can hold more than one value at a time.

# storing the cars in a single variables could look like this:

#car1 = "Ford"
#car2 = "Volvo"
#car3 = "BMW"

# However, what if you want to loop through the cars and find a specific one?
#  And what if you had not 3 cars, but 300?


# The solution is an array!

# An array can hold many values under a single name, and you can access the values by referring to an index number.

# Access the elements by referring to the index number 
# You refer to an array element by referring to the index number.


# Get the value of the first array item:

cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)



# Modifying the value of the first array item:

cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota" # Replacing the first index with "Ford"
print(cars) 


# The length of an Array

# Use the len() method to return the length of an array (the number of elements in an arra

# Return the number of elements in the cars array:

cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x) # 3 items 


# The length of an array is always one more than the highest array index.


# Looping Array Elements

# You can use the for in loop to loop through all the elements of an array.

cars = ["Volvo", "Toyota", "BMW"]
for x in cars:
    print(x)


# Adding Array Elemenet 
# Use ---append()-- to add an element to an array 

#Add one more element to the cars array:

cars = ["Volvo", "Toyota", "BMW"]
cars.append("Honda")
print(cars)

# Removing Array Elements

# Use pop() to remove an element from the array 

#Delete the second element of the cars array:

cars = ["Volvo", "Toyota", "BMW"]
cars.pop(1) # Note not as str by Integer for pop method
print(cars) 


# Also use remove()
# first occurrence of the specified value.

# Delete the element that has the value "Volvo":

cars = ["Volvo", "Toyota", "BMW"]
cars.remove("BMW") # Use a string not int
print(cars)

# Array Methods

# clear()	Removes all the elements from the list
cars = ["Volvo", "Toyota", "BMW"]
cars.clear()
print(cars)
# Output --- []

# copy()	Returns a copy of the list
cars = ["Volvo", "Toyota", "BMW"]
x = cars.copy()
print(x)
# Output --- ['Volvo', 'Toyota', 'BMW']


# count() Returns the number of elements with the specified value
cars = ["volvo", "Toyota", "BMW", "volvo"]
x = cars.count("volvo")
print(x)
# Output --- 2


# extend()	Add the elements of a list (or any iterable), to the end of the current list
# Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
# Output --- ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# index()	Returns the index of the first element with the specified value

# What is the position of the value "cherry":
fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")
print(x)
#Output --- 2


# insert()	Adds an element at the specified position

fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")
print(fruits)


# reverse()	Reverses the order of the list

# Reverse the order of the fruit list:
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()
print(fruits)
# Output --- ['cherry', 'banana', 'apple']


# sort()	Sorts the list
# Sort the list alphabetically:

cars = ['Ford', 'BMW', 'Volvo']

cars.sort()
print(cars)
# Output --- ['BMW', 'Ford', 'Volvo']

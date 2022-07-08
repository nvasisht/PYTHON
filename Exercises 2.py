
# Dictionaty Exercises

# Use the get method to print the value of the "model" key of the car dictionary.

from this import d


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
# It round brackets not Square


# Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car)

# Add the key/value pair "color" : "red" to the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car)
# not : instead =



# Use the pop method to remove "model" from the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)



# Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
# Output ---- {}



# IF.....Else

# Print "Hello World" if a is greater than b.

a = 50
b = 10
if a > b:
  print("Hello Wolrd")

# Print "Hello World" if a is not equal to b.

a = 50
b = 10
if a != b:
  print("Hello World")


# Print "Yes" if a is equal to b, otherwise print "No".

a = 50
b = 10
if a == b:
  print("Yes")
else: # i used elif
  print("No")


# Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".

a = 50
b = 10
if a ==b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")


# Print "Hello" if a is equal to b, and c is equal to d.

#if a ==b  and c ==d:
 # print("Hello World")

# Print "Hello" if a is equal to b, or if c is equal to d.

#if a ==b  or c ==d:
 # print("Hello")


# Use the correct short hand syntax to put the following statement on one line:

if 5 > 2: print("Five is greater than two!")


# Use the correct short hand syntax to write the following conditional expression in one line:

print("Yes") if 5 > 2 else print("No")



# WHOLE LOOPS:

# Print i as long as i is less than 6.

i = 1
while i < 6:
 print(i)
i += 1


# Stop the loop if i is 3.


i =1
while i < 6:
  if i ==3:
    break
  i +=1


#In the loop, when i is 3, jump directly to the next iteration.

i = 0 
while 1 <6:
  i +=1
  if i ==3:
   continue
print(1)


# Print a message once the condition is false.

i = 1
while i <6:
  print(i)
  i +=1
else:
  print("i is no longer less than 6")




# For Loops

# Loop through the items in the fruits list.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


# In the loop, when the item value is "banana", jump directly to the next item.

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x=="banana":
    continue
  print(x)

# Use the range function to loop through a code set 6 times.


for x in range(6):
  print(x)


# Exit the loop when x is "banana".
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x=="banana":
    break
  print(x)




# Python Lambda 

# Create a lambda function that takes one parameter (a) and returns it.

x = lambda a : a




# CLASSES AND OBJECTS 

# Create a class named MyClass:

class MyClass:
  x = 5

# Create an object of MyClass called p1:

class MyClass:
  x = 5
p1 = MyClass() # I missed a bracket

# Use the p1 object to print the value of x:

class MyClass:
  x = 5
p1 = MyClass()
print(p1.x) # Wasnt sure of the answer


# What is the correct syntax to assign a "init" function to a class?

class Person:
  def __init__ (self, name, age):
    self.name = name
    self.age = age




#Python Inheritances

#What is the correct syntax to create a class named 
# Student that will inherit properties and methods from
#  a class named Person?

# Answers 

# class Student(Person):


# What is the correct syntax to execute the 
# printname method of the object x?

class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()
# Output --- Mike




# Python Modules

# What is the correct syntax to import a module named "mymodule"?

import mymodule

# If you want to refer to a module by using a different name, you can create an alias.

#What is the correct syntax for creating an alias for a module?

import mymodule as mx

# What is the correct syntax of printing all variables and function names of the "mymodule" module?

import mymodule
print(dir(mymodule))

# What is the correct syntax of importing only the person1 dictionary of the "mymodule" module?

from mymodule import person1
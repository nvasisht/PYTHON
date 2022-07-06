
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a class
# To create a class, use the keyword class:

# Create a class named MyClass, with a property named x:

from argparse import _MutuallyExclusiveGroup
from unicodedata import name


class Myclass:
    x =5 
print(Myclass)
#Output ---- <class '__main__.Myclass'>

# Create Object
#Now we can use the class named MyClass to create objects:

# Create an object named p1, and print the value of x:

class  Myclass:
    x = 5
p1 = Myclass()
print(p1.x)
# Output --- 5

# The __init__() Function
# The examples above are classes and objects in their simplest form, 
# and are not really useful in real life applications.

# To understand the meaning of classes we have to
#  understand the built-in __init__() function.

# All classes have a function called __init__(),
#  which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:

# Create a class named Person, use the __init__() function
#  to assign values for name and age:

# Create class --- Person 
# __init__() --- values (name & age)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 25)
print(p1.name, p1.age)        

# Note: The __init__() function is called automatically every time
#  the class is being used to create a new object.


# Object Methods

# Objects can also contain methods. 
# Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:

# Insert a function that prints a greeting, and execute it on the p1 object:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print ("Hi! My name is " +  self.name )

p1 = Person("Jonh", 25)
p1.myfunc()


# The self parameter is a reference to the current instance of the class,
#  and is used to access variables that belong to the class.

# The self Parameter

# The self parameter is a reference to the current instance of the class,
#  and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, 
# but it has to be the first parameter of any function in the class:

# Use the words mysillyobject and abc instead of self:

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello, my name is " + abc.name)
p1=Person("Neha", 20)
p1.myfunc()

# Modify Object Properties

#You can modify properties on objects like this:

#Set the age of p1 to 40:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age= 40
print(p1.age)


# Delete Object Properties
# You can delete properties on objects by using the del keyword:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.age
print(p1.age)
# Output --- AttributeError: 'Person' object has no attribute 'age'



# Delete Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
print(p1)
# NameError: 'p1' is not defined


# The pass Statement

#class definitions cannot be empty,
#  but if you for some reason have a class definition with no content,
#  put in the pass statement to avoid getting an error.

class Person:
    pass

# Output --- # having an empty class definition like this, 
# would raise an error without the pass statement
# Output will be empty 


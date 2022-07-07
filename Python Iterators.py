
# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, 
# meaning that you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements the iterator protocol,
#  which consist of the methods __iter__() and __next__().

# Iterator vs Iterable

# Lists, tuples, dictionaries, and sets are all iterable objects.
#They are iterable containers which you can get an iterator from.

#All these objects have a iter() method which is used to get an iterator:

# Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects, and can return an iterator:

# Strings are also iterable objects, containing a sequence of characters:

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping through an Iterator

#Iterate the values of a tuple:

mytuple =("apple", "banana", "cherry")
for x in mytuple:
    print(x)


# Iterate the characters of a string: 

mystr = ("mango", "Kiwi", "orange")
for x in mystr:
    print(x)

#The for loop actually creates an iterator object
# and executes the next() method for each loop.


# Create an Iterator

# To create an object/class as an iterator you have to 
# implement the methods __iter__() and __next__()
# to your object.

# The __iter__() method acts similar, you can do operations (initializing etc.), 
# but must always return the iterator object itself.

# The __next__() method also allows you to do operations,
#  and must return the next item in the sequence.



# Create an iterator that returns numbers, 
# starting with 1, and each sequence will increase by one
#  (returning 1,2,3,4,5 etc.):

class Mynumbers:
    def __init__ (self):
        self.a = 1
        return self
    def __next__ (self):
        x = self.a 
        self.a +=1
        return x
myclass = Mynumbers() # An error, not understanding why
myiter = iter(myclass)

print(next(myiter))
# Output --- 1- 5



# StopIteration

# The example above would continue forever if you had 
# enough next() statements, or if it was used in a for loop.

#To prevent the iteration to go on forever, 
# we can use the StopIteration statement.

# In the __next__() method, we can add a terminating condition to raise an error 
# if the iteration is done a specified number of times:

class Mynumbers:
    def __init__ (self):
        self.a =1
        return self
    def __next__ (self):
        if self.a <=20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration
myclass = Mynumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
# Output --- 1 t0 20

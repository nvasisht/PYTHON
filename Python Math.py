# Python has a set of built-in math functions,
#  including an extensive math module,
#  that allows you to perform mathematical tasks on numbers.


# Built-in Math Functions
#The min() and max() functions can be used to find the
#  lowest or highest value in an iterable:

x = min (5, 10, 25)
y = max(5, 10, 25)

print(x) #Output 5
print(y) #Output 25



# The abs() function returns the absolute (positive) value
#  of the specified number:

x = abs(-7.25)
print(x) #Output --- 7.25


# The pow(x, y) function returns the value of x to the
#  power of y (xy).

# Return the value of 4 to the power of 3 
# (same as 4 * 4 * 4):

x = pow(4,3)
print(x) # Code does not support this language 



# The Math Module

# Python has also a built-in module called math,
#  which extends the list of mathematical functions.

# To use it, you must import the math module:

# import math 

# When you have imported the math module, you can
#  start using methods and constants of the module.

# The math.sqrt() method for example, 
# returns the square root of a number:

import math 
x = math.sqrt(64)
print(x) #Output --- 8.0


# The math.ceil() method rounds a number upwards to its nearest integer
# the math.floor() method rounds a number downwards to its nearest integer, 
# and returns the result:

import math 
x = math.ceil(14)
y = math.floor(1.4)
print(x)# returns 2 ---14
print(y) # return 1 ---1 


# The math.pi constant, returns the value of PI (3.14...):
import math
x = math.pi
print(x)
# Output 3.141592653589793

import math
x = math.pi/20
print(x)
#Output --- 0.15707963267948966
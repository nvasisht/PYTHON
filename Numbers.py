#There are numeric types:
#Int - whole number, positive or negative, without decimals, of unlimited length.
#Float -is a number, positive or negative, containing one or more decimals.
# Float can also be scientific numbers with an "e" to indicate the power of 10.
#Complex - written with a "j"

#Integers 
x=5
y=5
z=55
print(type(x))
print(type(y))
print(type(z))

#Float 

x=5.0
y=55e2
z=10.12e2
print(type(x))
print(type(y))
print(y)
print(type(z))


#Complex

x=5j
y=5+5j
z=-5j
print(type(x))
print(type(y))
print(y)
print(type(z))


#Type of conversion 

#Converting from one type to another (int), (float), (complex)

x=50
y=5.5
z=5j

#convert int to float 
a = float(x)

#convert int to complex
b = int(x)

#convert float to int
c = int(y)

print(a)
print(b)
print(c)

#You cant convert complex numebrs into any number type


#Random Number 
#Python does not have a random() function to make a random number,
#but Python has a built-in module called random that can be used to make random numbers:

##display a random number between 1 and 9

import random
print(random.randrange(1,100))

import random
print(random.randrange(1,5))

import random
print(random.randrange(1,20))


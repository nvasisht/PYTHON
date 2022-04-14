
#Operators are used to perform operations on variables and values.

#Using (+) operator to add together two values:

print(10 + 5)

#Python divides the operators in the following groups:

# ---------------------Arithmetic operators :--------------------------------------------------------------

# ---numeric values to perform common mathematical operations:
# (+) Addition
#  (-) Subtration 
# (*) Multiplication
# (/) Division
# (%) Modulus
print(5%5)
print(4%5)
print(50%70)
# (**) Exponetiation
print(5**5)
print(4**5)
print(50**70)
# (//) Floor Division
print(5//5)
print(4//5)
print(50//70)

#------------------------Assignment operators-------------------------------------------------------

# Are used to assign values to variables:
# Operator	Example	        Same As	
# =	        x = 5	          x = 5	
# +=      	x += 3      	  x = x + 3	
# -=      	x -= 3	          x = x - 3	
# *=	    x *= 3         	  x = x * 3	
# /=        x /= 3	          x = x / 3	
# %=	    x %= 3	          x = x % 3	
# //=	    x //= 3	          x = x // 3	
# **=	    x **= 3    	      x = x ** 3	
# &=	    x &= 3	          x = x & 3	
# |=	    x |= 3	          x = x | 3	
# ^=        x ^= 3	          x = x ^ 3	
# >>=	    x >>= 3	          x = x >> 3	
# <<=	    x <<= 3	          x = x << 3



#--------------------------Comparison operators--------------------------------------------------------

# Are used to compare two values:

# (==) Equal
print(5==5)

# (!=) Not equal 
print(5!=4)
print(4!=5)

# (>) Greater than
print(8>7)
print(6 >7) #False

# (<) Less than
print(6<7)
print(7<6) #False

# (>=) Greater than or equal to 
print(7>=6)
print(6>=7) #False

# (<=) Less than or equal to 
print(7<=6) #False
print(6<=7) 


#----------------------------Logical operators---------------------------------------

# Used to combine conditional statements:

# and ---- Returns True if BOTH statement are true

x = 5

print(x > 3 and x < 10)

# returns True because 5 is greater than 3 AND 5 is less than 10


# or  --- Returns True if one of the statements are true

x = 5

print(x > 3 or x < 4)

# returns True because one of the conditions are true (5 is greater than 3, but 5 is not less than 4)


# not --- Reverse the result, returns False if the result is true

x = 5

print(not(x > 3 and x < 10))

# returns False because not is used to reverse the result


#-------------------Identity operators----------------------------------------------

# used to compare the objects, not if they are equal,
#  but if they are actually the same object, with the same memory location:

# is  ------ Return True is both variable are the same object 

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


# is not ------- Returns True is both variable are not the same object 

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


#------------------------------Membership operators---------------------------------

# Used to test if a sequence is presented in an object:

# in ----- Returns True if a sequence with the specified value is present in the object 

x = ["apple", "banana"]

print("banana" in x)

# returns True because a sequence with the value "banana" is in the list


x = ["apple", "banana"]

print("cherry" in x) # Returns False because a sequence is not within the list 


# not in ----- Returns True if a sequence with the specified value is not present in the object 

x = ["apple", "banana"]

print("pineapple" not in x)
print("cherry" not in x)

# returns True because a sequence with the value "pineapple" is not in the list



#----------------------------------Bitwise operators--------------------------------

# Used to compare (binary) numbers:

# ( & )	AND --- Sets each bit to 1 if both bits are 1
# ( | )	OR ---	Sets each bit to 1 if one of two bits is 1
# ( ^ )	XOR ---	Sets each bit to 1 if only one of two bits is 1
# ( ~ )	NOT ---	Inverts all the bits
# ( << )	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# ( >> )	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
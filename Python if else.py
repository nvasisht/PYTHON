
# Python Conditions and If statements

# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
#  Greater than: a > b
# Greater than or equal to: a >= b

# These conditions can be used in several ways, 
# most commonly in "if statements" and loops.

# An "if statement" is written by using the --if-- keyword.

# If statement:


a = 33
b = 200
if b > a:
    print('b is greater than a')


# Indentation 

# Python relies on indentation (whitespace at the beginning of the line)
# to define scope in the code. Other programming languages uses {}

# If statement, without indentation (will raise an error):

#a = 33
#b = 200
#if b > a:
#print("b is greater than a") # you will get an error
# ^ IndentationError


# Elif

# The elif keyword is pythons way of saying "if the previous 
# conditions were not true, then try this condition"

a = 33
b = 33
if b > a:
    print("b is greater than a") # condition is not true
elif a==b:
    print("a and b are equal")



# Else

# The else keyword catches anything which isnt caught by preceding 

a = 33
b = 33
if b > a:
    print("b is greater than a") # condition is not true
elif a==b:
    print("a and b are equal") # If condition is not true
else:
    print("a is greater than b")

# Output ---- a and b are equal

# You can also have --else-- without elif

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  




# Short Hand IF.....Else

# If yoy have only one statement to execute, one for if, and one for else,
# You can put it all on the same line:

# One line if else statement:

a = 2
b = 330
print("A") if a > b else print("B")
# Output --- b is greater 

# This technique is known as Ternary Operators, or Conditional Expressions.

# You can also have multiple else statements on the same line:

# One line if else statement, with 3 conditions:

a = 330
b = 330
print("A") if a < b else print("=") if a ==b else print("B")

# And

# The and keyword is a logical operator, and is used to combine conditional statements:


# Test if a is greater than b, AND if c is greater than a:
a =200
b= 33
c = 500
if a > b and c > a:
    print("both conditions are True")



# OR 

#The or keyword is a logical operator, and is used to combine conditional statements:

# Test if a is greater than b, OR if a is greater than c:

# One of the conditon is TRUE
a =200
b= 33
c = 500
if a > b or a > c:
    print("At least of the contions is True which is a > b")


# Nestef If
# You can have if statements inside if statements, this is called nested if statements.

x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("also way above 20!")
    else:
        print("but not above 20.")


# The pass statement

# If statements cannot be empty, but if you for some reason have an if statement
# with no content, put in the --pass--statement to avoid getting an error

a = 33
b = 200

if b > a:
    pass

# having an empty if statement like this, 
# would raise an error without the pass statement

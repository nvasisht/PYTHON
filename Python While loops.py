# Python loops 

# Python has two primitive loops commands:
# While loops
# For loops

# While Loop 

# we can execute a set of statements as long as a condition is true.

# Print i as long as i is less than 6:

i = 1
while 1 < 6:
    print (i)
    i +=1

# Remeber to increment 1, or else the loop will continue forever

# The while loop requires relevant variables to be ready,
# in this example we need to define an indexing variable, i, which we set to 1.


# The break statement 

# with the break statement we can stop the loop even if the while condition is true:

# Exist the loop while i is 3:

i=1
while i < 6:
    print (i)
    if i==3:
        break 
    i +=1

# The continue statement
# With the continue statement we cab stop the current iteraction and contiue the the next:

# Continue to the next iteration if i is 3:

i = 0
while i<6:
    i +=1
    if i ==3:
        continue
    print(1)

# The else Statement 

# with the esle statement we can run a block of code when the condition no longer is true:

# Print a message once the condition is false:

i =1
while 1 <6:
    print(i)
    i +=1
else:
    print("i is no longer less than 6")
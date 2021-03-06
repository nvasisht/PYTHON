#DATA TYPES 
x = 5
print(type(x)) #int
x = "Hello World"
print(type(x)) #str 
x = 20.5
print(type(x)) #float
x = ["apple", "banana", "cherry"]
print(type(x)) #tuple 
#correct answer is list
x = ("apple", "banana", "cherry")
print(type(x)) #tuple
x = {"name" : "John", "age" : 36}
print(type(x)) #dict uses (:)
x = True
print(type(x)) #bool

#PYTHON SYNTAX
print("Hello World") 

if 5 > 2:
 print("Five is greater than two!") #spaces - Indentations


 #PYTHON COMMENTS
 # This is a comment 
 """ This is a comment
written in 
more that just one line """
#Use a multiline string to make the a multi line comment


#PYTHON VARIABLE 
#Create a variable named carname and assign the value Volvo to it.
carname ="Volvo" 
print(carname)

#Create a variable named x and assign the value 50 to it.
x = 50
print(x)

#Display the sum of 5 + 10, using two variables: x and y.
x = 5
y =10
print(x + y)

#Create a variable called z, assign x + y to it, and display the result.
x=5
y=10
z=x + y
print(z)

#Remove the illegal characters in the variable name:4

#2my-first_name = "John"
my_first_name = "John"
 
#Insert the correct syntax to assign the same value to all three variables in one code line.

x=y=z="oranges"

#Insert the correct keyword to make the variable x belong to the global scope
def myfunc():
    global x
    x ="Fantastic"
print(x)


#NUMBERS 

#Insert the correct syntax to convert x into a floating point number.

x = 5 #int
x = float(x) 
print(x)

#Insert the correct syntax to convert x into a integer.

x=5.5
x= int(x)
print(x)


#Insert the correct syntax to convert x into a complex number.

x=5
x=complex(x)
print(x)


#STRINGS

#Use the len method to print the length of the string.

x = "Hello World"
print(len(x))


#Get the first character of the string txt.

txt = "Hello World"
x = txt[0]
print(x)

# Get the characters from index 2 to index 4 (llo).

txt = "Hello World"
x = txt[2:4] #I was wrong it is [2:5]
print(x)


#Return the string without any whitespace at the beginning or the end.

txt = " Hello World "
x = txt.strip()   #Still struggling 
print(x)


#Convert the value of txt to upper case.

txt = "Hello World"
x = txt.upper()
print(x)

#Convert the value of txt to lower case.

txt = "Hello World"
x = txt.lower()
print(x)


#Replace the character H with a J.

txt= "Hello World"
txt = txt.replace('H', 'J')
print(txt)

#Insert the correct syntax to add a placeholder for the age parameter.
#String Format

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))



#BOOLEAN 

print(10>9) #True
print(10==9) #False
print(10<9) #True ---- wrong answer False

print(bool("abc")) #True
print(bool(0)) #False 


# OPERATORS

# Multiply 10 with 5, and print the result.
print(10*5)

# Divide 10 by 2, and print the result.
print(10/2)

# Use the correct ---membership operator--- to check if "apple" is present in the fruits object.

fruits = ["apple", "banana"]
if "apple" in fruits:
 print ("Yes, apple is a fruit!")


# Use the correct comparison operator to check if 5 is not equal to 10.

if 5 != 10:
  print("5 and 10 is not equal")

# Use the correct logical operator to check if ----at least one of two statements is True.-----

if 5 == 10  or 4 == 4:
  print("At least one of the statements is true")



#PYTHON LISTS

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Change the value from "apple" to "kiwi", in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits[0]="kiwi"
print(fruits)

#Use the append method to add "orange" to the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

#Use the insert method to add "lemon" as the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon") #missed a 1
print(fruits)


#Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana") 
print(fruits)


#Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits [-1]) #wasnt sure 

#Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5 ]) # i wrote 3 instead of 2


#Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits)) # i wrote fruits(len)




# PYTHON TUPLES

# Print the first item in the fruits tuple 

fruits = ("apple", "banana", "cherry")
print(fruits[0])

# Use the correct syntax to print the number of items in the fruits tuple.

fruits = ("apple", "banana", "cherry")
print(len(fruits))


#Use negative indexing to print the last item in the tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])


#Use a range of indexes to print the third, fourth, and fifth item in the tuple.

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])




# SETS 

# Check if "apple" is present in the fruits set.

fruits = {"apple", "banana", "cherry"}
if "apple"in fruits:
  print("Yes, apple is a fruit!")


# Use the add method to add "orange" to the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)


# Use the correct method to ---add multiple items--- (more_fruits) to the fruits set.

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits) 
# I wasn't sure


# Use the remove method to remove "banana" from the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

# Use the discard method to remove "banana" from the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)




#Surronded by either single or double quotations ('') or (" ")

#Assigned string to a variable 

#Done by a variable name followed by an equal sign and string 
# STEP 1 ------ a is a variable name
# STEP 2 ------ =
# STEP 3 -------  String 

a = "Hello"
print (a)

#Multiline Strings

#Assign string to a variable using three (3) quotes (""") or (''')

a = ''' Learning Python is fun and challenging at the same time '''
print (a)
# The line breaks are inserted at the same position as in the code.



#String are ARRAYS

#strings in Python are arrays of bytes representing unicode characters
#Python does not have a character data type, a single character is string with a length of 1

#[] can be used to access elements of string.
 #Get the character at position 1 (remember that the first character has the position 0):

#Every letter and space are counted from 0 to n depending when it ends

a = "Hello, World!"
print(a[1])
print(a[4])
print(a[7])
print(a[12])
#print(a[13]) #Cause an error --- string index out of range

#Looping through Strings

#Loop through the character in a string with a for loop

for x in "banana!":
    print(x)

for y in "Python is FUN":
    print(y)


#String Length 
#To get the length of a string use len() function 
#The length of the empty string is 0 - t's used to retrieve the length of every data type.


b = "Hello, World!"
print(len(a))

#Check String 

#To check if a certian phrase of character or word is present in a string, we use -in-

text = "The best things in life are free stuff!"
print("free" in text)
print("world" in text) # False - because it is not within the strings

# if Statement 

text = "The best things in life are free!"
if "free" in text:
    print("Yes , 'free' is present")
else :
    print("No, 'free' is not present") 


#Check if NOT 
#To check if a certain phrase or character or words is NOT present in a string use -not in-

text = "The best things in life are free!"
print("expensive " not in text)


#if Statement 
text = "The best things in life are free!"
if "expensive" not in  text:
    print("No, 'expensive' is NOT present")
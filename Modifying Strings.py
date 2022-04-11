
#Python has a set of bulit-in methods that you can use on strings

#Uppercase 

a = "Hello, Python!"
print(a.upper())

#Lowercase

a = "Hello, Lowercase!"
print(a.lower())


#Remove Whitespace 

a = " Hello, World! "
print(a.strip())   # returns "Hello, World!"


#Replace String 

#replace(0) method replace a string with another string 

a = "Hello, Replace!"
print(a.replace("H", "J"))


#Split String 

# Returns a list where the next text between the specified separator becomes the list items.

a = "Hello, split string"
print(a.split(", ")) #returns ['Hello', 'split string']

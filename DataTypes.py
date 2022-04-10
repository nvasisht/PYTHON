#   Built - in data types
# Variable can store data in different types
# Text type - string 
# Numeric types - int, float, complex
#Sequence type - list, tuple, range
# Mapping types - dict
# Set types - set, frozenset 
# Boolean type - bool
# Binary types - bytes, bytearray, memoryview 

#Data types of any obaject by using type() 

x = 5
print(type(x))

#String - "Hello Python"
#integer - 2 whole number
#Float - 2.0 Decimal 
#Complex - 1j
x = 5j
print(x)
#Sequence type
#List - ["apple", "banana"]
x =["apple", "banana"]
print(x)
#Tuple - ("apple", "cherry")
x =("apple", "cherry")
print(x)
#Range - range(6)
x= range(2)
print(x)
#Mapping Type
#Dict - {"name": "John","age": 25}
x = {"name": "John","age": 25}
print(x)
#Set types
#Set - {"orange", "kiwi"}
x=  {"orange", "kiwi"}
print(x)
#Frozenset - 
x = frozenset({"grapes", "pineapples"})
print(x)
#Boolean types - 
x = True
print(x)
#Binary Types
#Bytes 
x =b'Hello Python'
print(x)
#Bytearray
x=bytearray(5)
print(x)
#Memoryview
x =memoryview(bytes(5))
print(x)
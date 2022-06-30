
# Dictionaty Exercises

# Use the get method to print the value of the "model" key of the car dictionary.

from this import d


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))
# It round brackets not Square


# Change the "year" value from 1964 to 2020.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020
print(car)

# Add the key/value pair "color" : "red" to the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(car)
# not : instead =



# Use the pop method to remove "model" from the car dictionary.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)



# Use the clear method to empty the car dictionary.
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)
# Output ---- {}



# IF.....Else

# Print "Hello World" if a is greater than b.

a = 50
b = 10
if a > b:
  print("Hello Wolrd")

# Print "Hello World" if a is not equal to b.

a = 50
b = 10
if a != b:
  print("Hello World")


# Print "Yes" if a is equal to b, otherwise print "No".

a = 50
b = 10
if a == b:
  print("Yes")
else: # i used elif
  print("No")


# Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".

a = 50
b = 10
if a ==b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")


# Print "Hello" if a is equal to b, and c is equal to d.

#if a ==b  and c ==d:
 # print("Hello World")

# Print "Hello" if a is equal to b, or if c is equal to d.

#if a ==b  or c ==d:
 # print("Hello")


# Use the correct short hand syntax to put the following statement on one line:

if 5 > 2: print("Five is greater than two!")


# Use the correct short hand syntax to write the following conditional expression in one line:

print("Yes") if 5 > 2 else print("No")
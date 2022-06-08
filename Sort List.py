# Sort List Alphanumerically 

#List objects have a sort() method that will sort the list alphanumerically, 
# ascending, by default:


list = ["orange", "kiwi", "mango", "pineapple", "banana"]
list.sort()
print(list)

#Sort the list numerically:

numbers = [1000, 200, 5, 65, 9]
numbers.sort()
print(numbers)


# Sort Decending  --- from the bottom to the top

# Use reverse = True 
list = ["orange", "kiwi", "mango", "pineapple", "banana"]
list.sort(reverse=True)
print(list)

numbers = [1000, 1200, 5, 65, 9, 1200000]
numbers.sort(reverse= True)
print(numbers)


#Customize Sort Function 
#You can also customize your own function by using ---Key = funtion--

#The function will return a number that will be used
#  to sort the list (the lowest number first):

#Sort the list based on how close the number is to 50:

def myfunc(n):
    return abs(n -50)
numbers = [100, 50, 62, 82, 23]
numbers.sort(key= myfunc)
print(numbers)


# Case Insensitve Sort 

# Sort () is case senstive, 
# resulting in all capital letters being sorted before lower case:
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.sort()
print(fruits)


# Insensitive Case 
#case-insensitive sort function, use --str.lower-- as a key function

fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.sort(key=str.lower)
print(fruits)

# Reserve Order 
#The reverse() method reverses the current sorting order of the elements.
fruits = ["banana", "Orange", "Kiwi", "cherry"]
fruits.reverse()
print(fruits)

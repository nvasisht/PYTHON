
#Repesents one of two values : True & False

#True & Flase - are expression

print (10 < 9) # 9 is not less than 10 therefore it will be False
print( 10 > 9) #10 is greater then 9 therefore it will be True 
print(10 ==9 ) #False because the value is not the same (not equals to)
print(10==10) #True because the value are identical (equals to)

#CONDITONS
#if statement returns True or False

a = 200
b = 33

if a > b :
    print( "b is greater than a") #Fale
else: #Aavoid space
    print("b is not greater than a") #True

if a > b :
    print( "b is less than a") #
else: #Aavoid space
    print("b is not less than a")

#Evaluate Values and Variables

#The bool () function allows to evaluate any value and give True or False return 

#Evaluate a string and a number:

print (bool('Hello'))
print(bool(15))


#Evaluate two variable:

x = 'Hello'
y = 15
print(bool(x))
print(bool(y))


#Most values are TRUE 

#Almost any value is evaluated to TRUE if it has some sort of content

#Any string is TRUE except empty strings

#Any number is TRUE except 0

#Any list, tuple, set and dictionary are TRUE except empty ones


print(bool('abc'))
print(bool(123))
print(bool(["banaba", "apples", "cherry"]))



#Some values are FALSE

# Empty values such as (), [], {}, " 0", the number 0 and the value None

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))



#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a --class-- with a __len__ function that returns 0 or False:

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))



#function can Return a Boolean

def myFuntion():
    return True
print (myFuntion())


def myFuntion():
    return True
if myFuntion():
    print('YES!')
else: 
    print('NO!')
    
#Python also has many built-in functions that return a boolean
#  value, like the isinstance() function, which 
# can be used to determine if an object is of a certain data type:

# Check if an object is an integer or not:

x = 200
print(isinstance(x , int))

x = 200
print(isinstance(x , str))

x = 20.05
print(isinstance(x , float))

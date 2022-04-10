#Python syntax can be executed by writing directly in cmd or IDLE shell or VScode
print("Hello World")
print(type("Hello World"))


#Python Variable --- are containers for storing data values that can change 

#Python has no command before declaring a variable
#Every varaible is an object 

#Type of variables:
# Integers - whole numbers (int), Floats (decimals), Complex numbers (1j) & strings (single or double qoutes)

int (7)
print(int) #has no double qoutes

float(7.0)
print(float)

#Variable Name#

#Must stat with a letter (x) or underscore (_) or word (age)
#Cannot start with number 
#Contain alpha-numeric character or underscore (A-Z), (0-9) ,(_)
##There should be no space in a variable 

#Multi words variable names:
myvar='Green'
myvar2="Yellow"
_myvar='Purple'
MYVAR='Orange'
my_var_2="Red"
# Variable name is case-sentive 

#Camel case - myVariableName = "John"
#Pasel case - MyVariableName = "John"
#Snake case - my_variable_name = "John"

#Assign multiple values
#Many variable to multiple variables

x,y,z="orange", "banana", "cherry"
print(x)
print(y)
print(z)
print(x,y,z)

#One value to muitiple values
x=y=z = "orange", "banana", "cherry"
print(x)
print(y)
print(x,y,z)

#Unpack Collection 
#If you have a collection of value in a list, type
#Python allows you to extract values into variables - unpacking 
fruits=["apple", "banana", "cherry"]
x,y,z = fruits
print(x)
print(y)
print(z)
print(x,y,z)

#Output Varaibles

#print() - main output

#Comma - print(x,y,z)
# + operator to output multiple variable print(x+y+z)
# + character works as mathematical operator

x=20
y=10
print(x+y)

#Combining a string & numbers with + operator 

x=5
y="John"
print(x+y) #This was an error because you cant mix interger and string 

#Global Variable 

#Variable can also be created outside of function both inside & outside 
#Create a gloabl variable inside as function 

x = "awesome"
def myfunc():
    print("Python is" + x)
    myfunc()
print("Python is" + x)



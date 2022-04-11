
#We cannot combine strings and numbers 

#age = 36
#txt = "My name is John, I am " + age
#print(txt)

#Although we can use Format() method which takes passed arguments, foramt them and place them in the string where the placeholders are {}

age = 36
txt = "My name is John, I am {}"
print(txt.format(age))



#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



#Index Numbers

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:

quantity = 3 # 0
itemno = 567  # 1
price = 49.95   # 2
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
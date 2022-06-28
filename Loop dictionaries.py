# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Print all key names in the dictionary, one by one:
# Key names are brand, model & year
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)

# Print all the values in the dictionary, one by one 
# Values are Ford, Mustang, 1964
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(thisdict[x])


# Can use ---values() method to return values of dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
    print(x)
#Print both the key names and values


# Use --key() to return the keys of a dictionary

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
    print(x)
# Output --- brand, model, year


# Loop through both keys and values by using items()

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
    print(x,y)
# Output 
#brand Ford
#model Mustang
#year 1964
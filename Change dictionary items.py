# You can change the values of specific items by referring to its key name:

# Change the 'year' to 2018:

thisdist = {
    "brand" : "Ford",
    "model" : "Mustang",
    "Year" : 1964
}
thisdist["Year"] = 2018
print(thisdist)


# UPDATE ()

# The update () method will update the dictionary with the items
# from the given argument

#  This argument must be in a dictionary or iterable object with key pairs:

# # update the 'year' of car by using --update()-- method:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
car.update({"year":2020})
print(car)
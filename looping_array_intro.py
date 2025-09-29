#this is how you make a list
list_of_names = ["Zach","Tim","Betty"]

#lets say we want to add someone to our list of names
#we can use the .append() function in python to add new values

list_of_names.append("Jenny")

#the problem with dynamically adding data, is that we will not be able to always keep up with the index of our program.
#there are a couple of different solutions

#1. is to display all values in a list

for name in list_of_names:
    print(name)

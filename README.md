# Arrays and Lists in Python

Python does not have a typical "array" type.  It uses a data structure called a list.  A List uses many of the same features as an array, with some additional bonuses

## Typical Array Characteristics
- The same data type
- Fixed Length
- Add by index
- Loops mainly through loop iterable (count) variables

## Typical List Characteristics in Python
- Can be different data types (don't do this)
- Dynamic in length (no fixed size)
- Data is added to the list by either the index or through functions
- Can be looped using typical count variables, or by the built-in for-in loop structure
- Has some really cool features in functions for ease of use (searching and sorting)

# Syntax to work with lists
To make a list in python we can do the follwoing.  This is an empty list..we do not have to give it a size

```python
my_list = []
```
If we want to intialize a list with some data, we can do so by just adding the data inside of the brackets

```python
groceries = ["apple","orange","milk"]
```

We can still grab things from a list using it's index value.  Python index always starts at 0

```python
print(groceries[0])  #this would print out apple
```

You can also modify a list by calling its index value

```python
groceries[0] = "grape"
```

## Adding to a List
Adding to a list is a bit different then using a typical array in another language (or flowcharting). Since a list in Python is dynamic in size, we can add data to it at anytime without worry about the number of slots we need for elements in the array.  This is where cool functions/methods in Python come in

A list has several built in functions to help ease the use of them in Python.

For instance, the append() method/function allows us to add items to a list at any time.  The data we append to the list is added at the end of the list, and put in between the ()

```python
my_list.append("Zach")
```

## Looping Through Lists
If we want to modify or grab all the values in a list, we can use a loop.  In python there are several ways we can do this.  If we are just grabbing data, the typical to do this in python is a for in loop

The syntax looks like the following

```
for single_item in my_list:
    print(single_item)
```
What we are actually doing here is creating a variable name (called single_item) that represents an single item in the list.  Then we loop through each of the items, and print them out one a time.

Python example

```python
for name in my_list:
    print(name)
```

## Modifying Lists With Loops
Modifying a list is a little different than arrays.  By default, using a for in loop will not allow you to modify the list permanently.  You can grab each value and modify it, but the list values would remain the same.

There are two solutions to this:

1. Use a for-in loop and append the new values to a new list:

```python
test_scores = [45,69,90,77]
new_scores = []

#add five points to each score
for score in test_scores:
    score = score + 5
    new_scores.append(score)
```

2. Modify the original list to hold new values.  We use a more tradition for loop (for in range) for this:

```python
for i in range(len(test_scores)):
    test_scores[i] = test_scores[i] + 5
```

## Using Inputs with Lists
To use inputs with lists, we can just have the input be a flag for a loop.  Look at the following example:

```python
#we can use inputs to append test scores in this case
#we just ask the question and create a flag to exit when done
#in our case we can use -1 to exit
#then maybe we can get a class average for the test scores
average = 0
sum = 0
test_scores = []
tscore_inputs = float(input("Please enter a value for test scores.  When done press and enter -1 "))


while tscore_inputs != -1:
    test_scores.append(tscore_inputs)
    tscore_inputs = float(input("Please enter another number or -1 to exit "))

for score in test_scores:
    sum = sum + score

average = sum / len(test_scores)
print("The class average is", average)
```
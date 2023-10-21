# Python Data Structures and Loops

This document provides a comprehensive guide on various Python data structures such as lists and tuples, and covers loops and list comprehensions.

## Youtube link 
2 hours live session: https://youtube.com/live/53NX6h-ZENc

## Table of Contents
1. [Lists](#lists)
2. [For Loop](#for-loop)
3. [Else with For Loop](#else-with-for-loop)
4. [List Comprehension](#list-comprehension)
5. [Tuples](#tuples)
6. [Methods](#methods)

## Lists
A list in Python is a collection of items which can be of different types. Lists are ordered, changeable, and allow duplicate values.

### Example:
```python
my_list = [1, 2, 3, 4, 5]
print(my_list)
```

## For Loop
A for loop in Python is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

### Example:
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

## Else with For Loop
The else keyword in a for loop specifies a block of code to be executed when the loop is finished.

### Example:
```python
for x in range(5):
  print(x)
else:
  print("Finished!")
```

## List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

### Example:
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
```

## Tuples
A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.

### Example:
```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
```

## Methods
Here are some commonly used methods for lists and tuples:

### List Methods:
- `append()`: Adds an element at the end of the list
- `extend()`: Add the elements of a list (or any iterable), to the end of the current list
- `remove()`: Removes the first item with the specified value

### Tuple Methods:
- `count()`: Returns the number of times a specified value occurs in a tuple
- `index()`: Searches the tuple for a specified value and returns the position of where it was found


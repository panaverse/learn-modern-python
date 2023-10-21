# Python Lists and Their Methods

In this guide, we'll explore Python lists, their features, and the available methods. Lists are one of the most versatile and commonly used data types in Python.

## Youtube link 
2 hours live session: https://youtube.com/live/NzFLZkVtwMw

## Table of Contents

1. [Introduction to Lists](#introduction-to-lists)
2. [Indexing](#indexing)
3. [Slicing](#slicing)
4. [Positive and Negative Indexing](#positive-and-negative-indexing)
5. [List Methods in Python](#list-methods-in-python)

## Introduction to Lists

A list in Python is an ordered collection of items. Lists can contain a mix of different data types, including numbers, strings, and other lists. Lists are created by placing the items inside square brackets `[]`, separated by commas.

Example:
```python
fruits = ["apple", "banana", "cherry"]
```

## Indexing

You can access individual items in a list using an index. Indices start at 0 for the first item, 1 for the second, and so on.

Example:
```python
print(fruits[0])  # Outputs: apple
```

## Slicing

Slicing allows you to obtain a subset of items from a list. The syntax for slicing is `list[start:stop:step]`.

Example:
```python
print(fruits[1:3])  # Outputs: ['banana', 'cherry']
```

## Positive and Negative Indexing

- **Positive Indexing**: Starts from the beginning of the list.
  
  Example:
  ```python
  print(fruits[1])  # Outputs: banana
  ```

- **Negative Indexing**: Starts from the end of the list.
  
  Example:
  ```python
  print(fruits[-1])  # Outputs: cherry
  ```

## List Methods in Python

Python lists come with a set of built-in methods:

- `append()`: Adds an element to the end of the list.
- `clear()`: Removes all elements from the list.
- `copy()`: Returns a copy of the list.
- `count()`: Returns the number of elements with the specified value.
- `extend()`: Adds elements from another list (or any iterable) to the current list.
- `index()`: Returns the index of the first element with the specified value.
- `insert()`: Adds an element at a specified position.
- `pop()`: Removes the element at a specified position.
- `remove()`: Removes the first item with the specified value.
- `reverse()`: Reverses the order of the list.
- `sort()`: Sorts the list.

For more details and examples on each method, refer to the [official Python documentation](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).


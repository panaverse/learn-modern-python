# Python Guide

## Table of Contents
1. [Pass by Reference vs Pass by Value](#pass-by-reference-vs-pass-by-value)
2. [Mutable and Immutable Variables](#mutable-and-immutable-variables)
3. [Runtime Error Classes](#runtime-error-classes)
4. [Try-Except-Else-Finally Block](#try-except-else-finally-block)

---
## YouTube link
[2 hour live session](https://www.youtube.com/watch?v=LZNDpK-hhYU)


## Pass by Reference vs Pass by Value
In Python, the way variables are passed to functions can be thought of as "pass by object reference". This means that the function receives a reference to the object, not a copy of the object. However, the behavior can seem like "pass by value" or "pass by reference" depending on whether the object is mutable or immutable.

### Example: Pass by Value (with Immutable Types)
```python
def modify_value(num: int):
    print("Inside function (before modification):", id(num))
    num = 10
    print("Inside function (after modification):", id(num))

x = 5
print("Before function call:", id(x))
modify_value(x)
print("After function call:", id(x))
```

In this example, `x` is an integer (which is immutable). When we pass `x` to the function and modify it inside the function, the `id` (memory address) of `num` inside the function changes, indicating that a new integer object has been created. The `id` of `x` outside the function remains the same.

### Example: Pass by Reference (with Mutable Types)
```python
def modify_list(lst: list):
    print("Inside function (before modification):", id(lst))
    lst.append(4)
    print("Inside function (after modification):", id(lst))

my_list = [1, 2, 3]
print("Before function call:", id(my_list))
modify_list(my_list)
print("After function call:", id(my_list))
```

In this example, `my_list` is a list (which is mutable). When we pass `my_list` to the function and modify it inside the function, the `id` of `lst` inside the function remains the same, indicating that the same list object is being modified. The `id` of `my_list` outside the function also remains the same.

---

## Mutable and Immutable Variables
Variables in Python can be either mutable or immutable.

- **Mutable types** can be changed after they are created. Examples include lists, dictionaries, and sets.
- **Immutable types** cannot be changed after they are created. Examples include integers, floats, strings, and tuples.

### Example: Mutable Type
```python
my_list = [1, 2, 3]
print("Before modification:", my_list, "id:", id(my_list))
my_list.append(4)
print("After modification:", my_list, "id:", id(my_list))
```

In this example, the list `my_list` is modified in place, and its `id` remains the same.

### Example: Immutable Type
```python
my_string = "hello"
print("Before modification:", my_string, "id:", id(my_string))
my_string = my_string + " world"
print("After modification:", my_string, "id:", id(my_string))
```

In this example, when we modify `my_string`, a new string object is created, and the `id` of `my_string` changes.

---

## Runtime Error Classes
Python has several built-in error classes to handle runtime errors. Here are examples of some common runtime errors:

### IndexError
Occurs when trying to access an index that is out of range.

```python
try:
    my_list = [1, 2, 3]
    print(my_list[3])  # This will raise an IndexError
except IndexError as e:
    print("Caught an IndexError:", str(e))
```

### ZeroDivisionError
Occurs when dividing by zero.

```python
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print("Caught a ZeroDivisionError:", str(e))
```

---

## Try-Except-Else-Finally Block
The `try-except-else-finally` block in Python is used for exception handling.

- The `try` block contains the code that may raise an exception.
- The `except` block contains the code that is executed if an exception is raised.
- The `else` block contains the code that is executed if no exceptions are raised.
- The `finally` block contains the code that is always executed, regardless of whether an exception is raised.

```python
try:
    numerator = 10
    denominator = 2
    result = numerator / denominator
except ZeroDivisionError as e:
    print("Caught a ZeroDivisionError:", str(e))
else:
    print("Division successful:", result)
finally:
    print("This block is always executed")
```


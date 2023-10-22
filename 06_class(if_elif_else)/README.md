# Python Control Flow and Typing Guide

This guide provides an overview of Python's control flow structures including if, if-else, if-elif-else, and nested if-else-elif statements. Additionally, it covers the use of Python's static type variables, the `Union` and `Optional` types from the `typing` module, the `zip` function with lists, and sorting a list of tuples based on the second tuple index.

## Youtube link 
2 hours live session: https://youtube.com/live/ASNTpFSQHPo

## Table of Contents

- [If Statement](#if-statement)
- [If-Else Statement](#if-else-statement)
- [If-Elif-Else Statement](#if-elif-else-statement)
- [Nested If-Else-Elif](#nested-if-else-elif)
- [Static Type Variables](#static-type-variables)
- [Union and Optional Types](#union-and-optional-types)
- [Zip Function with Lists](#zip-function-with-lists)
- [Sorting a List of Tuples](#sorting-a-list-of-tuples)

## If Statement

```python
x: int = 10
if x > 5:
    print("x is greater than 5")
```

## If-Else Statement

```python
x: int = 4
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
```

## If-Elif-Else Statement

```python
x: int = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## Nested If-Else-Elif

```python
x: int = 10
y: int = 5
if x > 5:
    if y > 5:
        print("x and y are both greater than 5")
    else:
        print("x is greater than 5 but y is not")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

## Static Type Variables

In Python 3.6 and later, you can use static type annotations to indicate the expected type of a variable.

```python
x: int = 10
y: str = "Hello"
z: float = 3.14
```

## Union and Optional Types

`Union` allows a variable to be one of several types. `Optional` is a shorthand for `Union[T, None]`.

```python
from typing import Union, Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello, Guest!"
    else:
        return f"Hello, {name}!"

age: Union[int, str] = "Twenty"
print(greet())
print(greet("John"))
```

## Zip Function with Lists

The `zip` function is used to combine two or more iterables.

```python
names: list[str] = ["Alice", "Bob", "Charlie"]
ages: list[int] = [25, 30, 35]

zipped = zip(names, ages)
for name, age in zipped:
    print(f"{name} is {age} years old")
```

## Sorting a List of Tuples

You can sort a list of tuples based on the second tuple index using the `sorted` function.

```python
tuples: list[tuple[str, int]] = [("Alice", 25), ("Bob", 30), ("Charlie", 20)]
sorted_tuples = sorted(tuples, key=lambda x: x[1])
print(sorted_tuples)  # Output: [('Charlie', 20), ('Alice', 25), ('Bob', 30)]
```

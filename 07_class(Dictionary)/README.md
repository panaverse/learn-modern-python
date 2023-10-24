# Python Static Typing for Dictionaries

This guide demonstrates the creation of dictionaries in Python using static typing. We'll explore dictionaries with different hashable key types and values of type `Any`, `Optional`, and `Union`. Additionally, we'll use dictionary comprehensions and demonstrate swapping keys and values.

## YouTube link
[2 hour live session](https://youtube.com/live/u0K3m7ZAUnI)

## Table of Contents
1. [Setting up Static Typing](#setting-up-static-typing)
2. [Creating Dictionaries](#creating-dictionaries)
    - [Using `Any` Type](#using-any-type)
    - [Using `Optional` Type](#using-optional-type)
    - [Using `Union` Type](#using-union-type)
3. [Dictionary Comprehensions](#dictionary-comprehensions)
4. [Swapping Keys and Values](#swapping-keys-and-values)

## Setting up Static Typing

To use static typing in Python, we'll need to import the required types from the `typing` module. For this guide, we're specifically interested in `Any`, `Optional`, and `Union`.

```python
from typing import Any, Optional, Union
```

## Creating Dictionaries

### Using `Any` Type

`Any` is the most flexible type. It can represent any type at all. Here's how to create a dictionary with keys of any hashable type and values of any type:

```python
from typing import Dict

my_dict: Dict[Any, Any] = {
    1: "one",
    "two": 2,
    (3, 4): [3, 4]
}
```

### Using `Optional` Type

`Optional` is a shorthand for a value that can either be of a specific type or `None`.

```python
from typing import Dict

my_optional_dict: Dict[Any, Optional[int]] = {
    1: 10,
    "two": None,
    (3, 4): 34
}
```

### Using `Union` Type

`Union` type allows us to specify that a value can be one of several types.

```python
from typing import Dict

my_union_dict: Dict[Any, Union[int, str]] = {
    1: "one",
    "two": 2,
    (3, 4): "three-four"
}
```

## Dictionary Comprehensions

Dictionary comprehensions provide a concise way to create dictionaries.

```python
squared_numbers = {i: i**2 for i in range(5)}
```

## Swapping Keys and Values

To swap the keys and values of a dictionary:

```python
swapped_dict = {v: k for k, v in my_dict.items()}
```

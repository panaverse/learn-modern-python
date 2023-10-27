# Python Functions Guide


Python functions are a cornerstone of the language, providing modularity and code reusability. 

- **Pre-defined Functions**: Python comes with a variety of built-in functions like `len()` that are ready to use without any additional imports.
- **User-defined Functions**: Users can define their own functions using the `def` keyword, allowing for customized functionality tailored to specific needs.
- **Arguments and Parameters**: Functions can accept inputs in the form of arguments, and these inputs are defined in the function signature as parameters.
- **Default Functions**: Parameters can be given default values, making them optional when the function is called.
- **Optional, Positional, and Keyword Arguments**: Functions can accept different types of arguments, including optional arguments with default values, positional arguments that depend on order, and keyword arguments that are specified by name.
- **Lambda Functions**: Anonymous functions can be defined on-the-fly using the `lambda` keyword.
- **Recursive Functions**: Functions can call themselves to solve problems in a recursive manner.
- **Decorators**: Functions can be wrapped by other functions to extend their behavior without modifying their code.
- **Functions with Unlimited Arguments**: Functions can be designed to accept an arbitrary number of arguments, either as positional arguments or keyword arguments.

By understanding and utilizing these different aspects of Python functions, developers can write cleaner, more efficient, and more maintainable code.



## Table of Contents
1. [Pre-defined Functions](#pre-defined-functions)
2. [User-defined Functions](#user-defined-functions)
3. [Arguments and Parameters](#arguments-and-parameters)
4. [Default Functions](#default-functions)
5. [Optional, Positional, and Keyword Arguments](#optional-positional-and-keyword-arguments)
6. [Lambda Functions](#lambda-functions)
7. [Recursive Functions](#recursive-functions)
8. [Decorators](#decorators)
9. [Functions with Unlimited Arguments](#functions-with-unlimited-arguments)

---

## YouTube link
[2 hour live session](https://youtube.com/live/Iztf55Cs4pw)

## Pre-defined Functions

Python provides several built-in functions that are readily available for use.

```python
# Example of a pre-defined function
result: int = len("Hello, World!")
print(result)  # Output: 12
```

---

## User-defined Functions

You can define your own functions in Python using the `def` keyword.

```python
def greet(name: str) -> None:
    print(f"Hello, {name}!")

greet("John")  # Output: Hello, John!
```

---

## Arguments and Parameters

Parameters are the variables listed inside the parentheses in the function definition, whereas arguments are the values passed to the function when it is called.

```python
def add(a: int, b: int) -> int:
    return a + b

result: int = add(5, 3)
print(result)  # Output: 8
```

---

## Default Functions

You can assign default values to parameters, making them optional during a function call.

```python
def power(base: int, exponent: int = 2) -> int:
    return base ** exponent

print(power(3))        # Output: 9
print(power(3, 3))     # Output: 27
```

---

## Optional, Positional, and Keyword Arguments

### Optional Arguments
Optional arguments are those that have a default value.

```python
def greet(name: str = "Guest") -> None:
    print(f"Hello, {name}!")

greet()            # Output: Hello, Guest!
greet("John")      # Output: Hello, John!
```

### Positional Arguments
Positional arguments are arguments that need to be included in the proper position or order.

```python
def subtract(a: int, b: int) -> int:
    return a - b

result: int = subtract(10, 5)
print(result)  # Output: 5
```

### Keyword Arguments
Keyword arguments are arguments passed to a function by explicitly specifying the name of the parameter.

```python
def divide(dividend: int, divisor: int) -> float:
    return dividend / divisor

result: float = divide(divisor=5, dividend=25)
print(result)  # Output: 5.0
```

---

## Lambda Functions

Lambda functions are anonymous functions defined using the `lambda` keyword.

```python
square: callable = lambda x: x * x
print(square(4))  # Output: 16
```

---

## Recursive Functions

A recursive function is a function that calls itself.

```python
def factorial(n: int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result: int = factorial(5)
print(result)  # Output: 120
```

---

## Decorators

Decorators are a way to modify or extend the behavior of a function.

```python
def my_decorator(func: callable) -> callable:
    def wrapper(*args, **kwargs) -> None:
        print("Something is happening before the function is called.")
        func(*args, **kwargs)
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello(name: str) -> None:
    print(f"Hello {name}!")

say_hello("John")
```

---

## Functions with Unlimited Arguments

You can define functions that accept an arbitrary number of arguments.

### Unlimited Positional Arguments

```python
def add(*numbers: int) -> int:
    return sum(numbers)

result: int = add(1, 2, 3, 4, 5)
print(result)  # Output: 15
```

### Unlimited Keyword Arguments

```python
def print_key_values(**kwargs: str) -> None:
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_key_values(name="John", age="30", country="USA")
```


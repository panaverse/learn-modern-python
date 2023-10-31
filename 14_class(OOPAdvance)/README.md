Covers the topics you mentioned, with explanations and Python code examples. This file is written with Markdown syntax and includes Python code blocks with static type annotations.



# Python Static Type Code Examples

This repository contains examples and explanations of various Python concepts, focusing on static type annotations.

## Table of Contents
- [Multiple Inheritance](#multiple-inheritance)
- [Function Overloading with @overload Decorator](#function-overloading-with-overload-decorator)
- [Method Overloading with @overload Decorator](#method-overloading-with-overload-decorator)
- [Method Overriding](#method-overriding)
- [Polymorphism](#polymorphism)
- [Using `__call__()`](#using-__call__)
- [The `object` Class](#the-object-class)

## YouTube link
[2 hour live session](https://youtube.com/live/kvvanowR0QM)

## Multiple Inheritance

Multiple inheritance allows a class to inherit from more than one base class.

```python
class Base1:
    def method(self) -> str:
        return "Base1"

class Base2:
    def method(self) -> str:
        return "Base2"

class Derived(Base1, Base2):
    pass

obj = Derived()
print(obj.method())  # Output: Base1
```

In the example above, `Derived` inherits from both `Base1` and `Base2`. Since `Base1` is listed first, its `method` is the one that gets called.

## Function Overloading with @overload Decorator

Function overloading allows defining multiple versions of a function with different types of parameters.

```python
from typing import overload

@overload
def add(x: int, y: int) -> int:
    ...

@overload
def add(x: float, y: float) -> float:
    ...

def add(x, y):
    return x + y

print(add(1, 2))        # Output: 3
print(add(1.5, 2.5))   # Output: 4.0
```

## Method Overloading with @overload Decorator

Method overloading can be achieved in a similar manner to function overloading.

```python
from typing import overload

class Calculator:
    @overload
    def add(self, x: int, y: int) -> int:
        ...
    
    @overload
    def add(self, x: float, y: float) -> float:
        ...
    
    def add(self, x, y):
        return x + y

calc = Calculator()
print(calc.add(1, 2))      # Output: 3
print(calc.add(1.5, 2.5))  # Output: 4.0
```

## Method Overriding

Method overriding allows a subclass to provide a specific implementation of a method that is already defined in its superclass.

```python
class Animal:
    def speak(self) -> str:
        return "Some generic animal sound"

class Dog(Animal):
    def speak(self) -> str:
        return "Bark"

dog = Dog()
print(dog.speak())  # Output: Bark
```

## Polymorphism

Polymorphism allows objects of different classes to be treated as objects of a common superclass.

```python
class Cat(Animal):
    def speak(self) -> str:
        return "Meow"

def animal_sound(animal: Animal) -> str:
    return animal.speak()

print(animal_sound(Dog()))  # Output: Bark
print(animal_sound(Cat()))  # Output: Meow
```

## Using `__call__()`

The `__call__()` method allows an object to be called like a function.

```python
class Multiplier:
    def __call__(self, x: int, y: int) -> int:
        return x * y

multiply = Multiplier()
print(multiply(3, 4))  # Output: 12
```

## The `object` Class

Every class in Python 3 implicitly inherits from the `object` class, which is the base class for all classes.

```python
class MyClass:
    pass

obj = MyClass()
print(isinstance(obj, object))  # Output: True
```

In this example, `MyClass` implicitly inherits from `object`, so an instance of `MyClass` is also an instance of `object`.
```

### Save to File

Would you like to save this `README.md` content to a file? If so, please provide a file name, and I will save it for you.

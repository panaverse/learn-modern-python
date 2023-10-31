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
``

# Dunder-Methods

## some common dunder methods in python and their usage

<table>
  <thead>
    <tr>
      <th>Dunder method</th>
      <th>Description</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>`__new__()`</td>
      <td>This method is called before any other constructor method is called. It is used to create a new object.</td>
      <td>`class MyClass(object): def __new__(cls, *args, **kwargs):     # Create a new object     obj = object.__new__(cls)     # Initialize the object     obj.__init__(*args, **kwargs)     return obj`</td>
    </tr>
    <tr>
      <td>`__init__()`</td>
      <td>This method is called to initialize a new object. It is typically used to set the attributes of the object.</td>
      <td>`class MyClass(object): def __init__(self, name):     self.name = name`</td>
    </tr>
    <tr>
      <td>`__del__()`</td>
      <td>This method is called when an object is garbage collected. It can be used to clean up any resources that the object is using.</td>
      <td>`class MyClass(object): def __del__(self):     # Clean up any resources     print("Deleting object {}".format(self.name))`</td>
    </tr>
    <tr>
      <td>`__repr__()`</td>
      <td>This method is called when the `repr()` function is used on an object. It returns a string representation of the object.</td>
      <td>`class MyClass(object): def __repr__(self):     return "MyClass('{}')".format(self.name)`</td>
    </tr>
    <tr>
      <td>`__str__()`</td>
      <td>This method is called when the `str()` function is used on an object. It returns a string representation of the object that is intended to be human-readable.</td>
      <td>`class MyClass(object): def __str__(self):     return "MyClass object with name '{}'".format(self.name)`</td>
    </tr>
    <tr>
      <td>`__getattr__()`</td>
      <td>This method is called when an attribute is accessed on an object that does not exist. It can be used to implement dynamic attribute lookup.</td>
      <td>`class MyClass(object): def __getattr__(self, name):     # Get the attribute from a dictionary     return self._dict[name]`</td>
    </tr>
    <tr>
      <td>`__setattr__()`</td>
      <td>This method is called when an attribute is set on an object. It can be used to implement validation or other logic before setting the attribute.</td>
      <td>`class MyClass(object): def __setattr__(self, name, value):     # Validate the value     if not isinstance(value, str):         raise ValueError("Attribute {} must be a string".format(name))     # Set the attribute     self._dict[name] = value`</td>
    </tr>
    <tr>
      <td>`__delattr__()`</td>
      <td>This method is called when an attribute is deleted from an object. It can be used to implement cleanup logic.</td>
      <td>`class MyClass(object): def __delattr__(self, name):     # Delete the attribute from a dictionary     del self._dict[name]`</td>
    </tr>
    <tr>
      <td>`__call__()`</td>
      <td>This method is called when an object is called like a function. It can be used to implement custom behavior for calling an object.</td>
      <td>`class MyClass(object): def __call__(self):     # Print a message     print("You called me!")`</td>
    </tr>
    <tr>
      <td>`__getitem__()`</td>
      <td>This method is called when an item is accessed on an object using the `[]` operator. It can be used to implement custom behavior for accessing items from an object.</td>
      <td>`class MyClass(object): def __getitem__(self, index):     # Get the item from a list     return self._list[index]`</td>
    </tr>
    <tr>
      <td>`__setitem__()`</td>
      <td>This method is called when an item is set on an object using the `[]` operator. It can be used to implement custom behavior for setting items in an object.</td>
      <td>`class MyClass(object): def __setitem__(self, index, value):     # Set the item in a list     self._list[index] = value`</td>
    </tr>
    <tr>
      <td>`__delitem__()`</td>
      <td>This method is called when an item is deleted from an object using the `del` statement. It can be used to implement cleanup logic.</td>
      <td>`class MyClass(object): def __delitem__(self, index):     # Delete the item from a list     del self._list[index]`</td>
    </tr>
    <tr>
      <td>`__iter__()`</td>
      <td>This method is called when an object is iterated over. It returns an iterator for the object.</td>
      <td>`class MyClass(object): def __iter__(self):     # Return an iterator for the list     return iter(self._list)`</td>
    </tr>
    <tr>
      <td>`__next__()`</td>
      <td>This method is called when the `next()` function is used on an iterator. It returns the next item in the iterator.</td>
      <td>`class MyClass(object): def __next__(self):     # Return the next item in the list     item = next(self._iter)     # Check if the item is the last item in the list     if item is None:         raise StopIteration()`</td>
    </tr>
  </tbody>
</table>



# __init__()
    class MyClass:
        def __init__(self, name):
            self.name = name
    
    my_object = MyClass("John")

# __new__()
    class MyClass:
        def __new__(cls, name):
            # Create a new object instance
            my_class_object = object.__new__(cls)
    
            # Initialize the object
            my_class_object.name = name
    
            return my_class_object

my_class_object = MyClass.__new__(MyClass, "John")

# __del__()
    class MyClass:
        def __del__(self):
            # Clean up the object
            print("Deleting object {}".format(self.name))
    
    my_object = MyClass("John")
    del my_object

# __repr__()
    class MyClass:
        def __repr__(self):
            return "MyClass({})".format(self.name)
    
    my_object = MyClass("John")
    print(repr(my_object))

# __str__()
    class MyClass:
        def __str__(self):
            return "MyClass object with name {}".format(self.name)
    
    my_object = MyClass("John")
    print(str(my_object))

# __getattr__()
      class MyClass:
          def __getattr__(self, name):
              # Get the attribute from a dictionary
              return self._dict[name]
      
      my_object = MyClass()
      my_object._dict["name"] = "John"
      print(my_object.name)

# __setattr__()
    class MyClass:
        def __setattr__(self, name, value):
            # Validate the value
            if not isinstance(value, str):
                raise ValueError("Attribute {} must be a string".format(name))
    
            # Set the attribute in a dictionary
            self._dict[name] = value
    
    my_object = MyClass()
    my_object._dict["name"] = "John"


# __delitem__()
      class MyClass:
          def __delitem__(self, index):
              # Delete the item from a list
              del self._list[index]
      
      my_object = MyClass([1, 2, 3])
      del my_object[0]
      print(my_object)

# __iter__()
      class MyClass:
          def __iter__(self):
              return iter(self._list)
      
      my_object = MyClass([1, 2, 3])
      for item in my_object:
          print(item)

# __next__()
      class MyClass:
        def __next__(self):
            # Return the next item in the iterator
            try:
                return self._list[self._index]
            except IndexError:
                raise StopIteration()
      
      my_object = MyClass([1, 2, 3])
      my_object._index = 0
      while True:
        try:
            print(my_object.__next__())
        except StopIteration:
            break



### Save to File

Would you like to save this `README.md` content to a file? If so, please provide a file name, and I will save it for you.

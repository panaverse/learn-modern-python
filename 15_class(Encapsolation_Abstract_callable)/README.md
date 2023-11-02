Example that includes explanations and Python static type code examples for access modifiers, encapsulation, abstract classes, and the special methods `__str__`, `__repr__`, and `__call__`. Finally, I will touch on how to create a Python package and upload it to PyPI.

Please note that as of my last update, Python's static typing relies on type hints (PEP 484), and actual enforcement of access modifiers like private and protected members is not strictly implemented in Python as it is in other languages like Java or C++.

---

## YouTube link
[2 hour live session](https://youtube.com/live/izU0RInhe8g)

# PythonPackageExample

This package demonstrates the basic concepts of object-oriented programming (OOP) in Python, including access modifiers, encapsulation, abstract classes, and special methods like `__str__`, `__repr__`, and `__call__`.

## Features

- **Access Modifiers:** Emulates private and protected members using name mangling.
- **Encapsulation:** Protects the internal state of objects through getters and setters.
- **Abstract Class:** Defines a blueprint for other classes with abstract methods.
- **Special Methods:** Implements `__str__`, `__repr__`, and `__call__` for class instances.
-- **Duck Typing**
Duck Typing: Employ Python’s dynamic typing feature that focuses on the presence of methods and properties, not the type of the object.

## Installation

Install the package using pip:

```bash
pip install PythonPackageExample
```

## Usage

Here's a basic usage example:

```python
from PythonPackageExample import MyClass

my_object = MyClass()
print(my_object)
```

## Examples

### Access Modifiers

In Python, access modifiers are not enforced by the language, but we follow a convention by prefixing the name with an underscore for protected members and double underscores for private members.

```python
class MyClass:
    def __init__(self):
        self.public_member = "This is public"
        self._protected_member = "This is protected"
        self.__private_member = "This is private"

    def __str__(self):
        return f"MyClass({self.public_member})"
```

### Encapsulation

We use property decorators to control the access to member variables.

```python
class EncapsulatedObject:
    def __init__(self):
        self._my_protected_var = 0
    
    @property
    def my_var(self) -> int:
        """Getter for my_var."""
        return self._my_protected_var

    @my_var.setter
    def my_var(self, value: int) -> None:
        """Setter for my_var."""
        if value < 0:
            raise ValueError("This variable cannot be negative.")
        self._my_protected_var = value
```

### Abstract Class

Abstract classes can't be instantiated and require subclasses to provide implementations for the abstract methods.

```python
from abc import ABC, abstractmethod

class AbstractClassExample(ABC):

    @abstractmethod
    def do_something(self):
        pass

class ConcreteClass(AbstractClassExample):
    
    def do_something(self):
        return "Doing something."
```

### Special Methods

Implement `__str__`, `__repr__`, and `__call__` to enhance the object's behavior.

```python
class SpecialMethodsExample:
    def __init__(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return f"SpecialMethodsExample with value {self.value}"
    
    def __repr__(self) -> str:
        return f"SpecialMethodsExample({self.value})"
    
    def __call__(self, *args, **kwargs):
        return f"Called with args: {args} and kwargs: {kwargs}"
```

## Duck Typing Example

In Python, duck typing is an application of the dynamic typing paradigm which does not look at an object's type itself but instead, the methods and properties that object has.

```python
class Duck:
    def quack(self):
        print("Quack, quack!")
    
    def walk(self):
        print("Walk like a duck.")

class Person:
    def quack(self):
        print("I'm Quacking like a duck!")
    
    def walk(self):
        print("I'm walking like a duck!")

def duck_test(animal):
    animal.quack()
    animal.walk()

# Duck Typing in action
duck = Duck()
person = Person()

duck_test(duck)   # Behaves like a duck
duck_test(person) # Also 'quacks' and 'walks' like a duck
```

The above code snippet does not concern itself with the type of the object passed to the function `duck_test`. Instead, it just calls the methods without checking the type. This is the essence of duck typing.

## Creating and Uploading a Package to PyPI

To create a Python package and upload it to PyPI, follow these steps:

1. **Organize your code** into a package structure.
2. **Write setup.py:** This is the build script for setuptools. It tells setuptools about your package (such as the name and version).
3. **Create a dist:** Build your package with the `python setup.py sdist bdist_wheel` command.
4. **Upload to PyPI:** Use `twine` to upload your distribution package to PyPI.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

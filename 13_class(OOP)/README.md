Explains the basic concepts of Object-Oriented Programming (OOP) in Python, including classes, methods, attributes, class variables, and inheritance. It also includes examples of an `Employee` class and its subclasses `Designer` and `Developer`, demonstrating the use of `super().__init__()` to initialize the parent class.

---

# Object-Oriented Programming in Python

## Table of Contents
1. [OOP Basic Concepts](#oop-basic-concepts)
2. [Classes, Methods, and Attributes](#classes-methods-and-attributes)
3. [Class Variables](#class-variables)
4. [Inheritance](#inheritance)
5. [Example: Employee, Designer, and Developer](#example-employee-designer-and-developer)


## YouTube link
[2 hour live session](https://youtube.com/live/l0PFRL58AZk)

## OOP Basic Concepts
Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects," which can contain data and code that manipulates that data. Objects are instances of classes, which can hold both data (attributes) and code (methods).

## Classes, Methods, and Attributes
- **Class**: A blueprint for creating objects.
- **Method**: A function defined inside a class.
- **Attribute**: A variable that belongs to an object.

### Example: Creating a Simple Class
```python
class Dog:
    def __init__(self, name, age):
        self.name = name  # Attribute
        self.age = age    # Attribute
    
    def bark(self):       # Method
        print("Woof!")
```

## Class Variables
Class variables are shared by all instances of a class. They are set by prefixing a variable with the name of the class.

### Example: Using Class Variables
```python
class Dog:
    species = "Canis familiaris"  # Class variable
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print("Woof!")
```

## Inheritance
Inheritance allows a class to inherit attributes and methods from another class.

### Example: Inheriting from a Base Class
```python
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def speak(self):
        print("Some generic sound")

class Dog(Animal):
    def bark(self):
        print("Woof!")
```

## Example: Employee, Designer, and Developer
Here, we define an `Employee` class and two subclasses `Designer` and `Developer`.

### Base Class: Employee
```python
class Employee:
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Department: {self.department}")
```

### Subclass: Designer
```python
class Designer(Employee):
    def __init__(self, name, age, department, tool):
        super().__init__(name, age, department)
        self.tool = tool
    
    def display_info(self):
        super().display_info()
        print(f"Design Tool: {self.tool}")
```

### Subclass: Developer
```python
class Developer(Employee):
    def __init__(self, name, age, department, language):
        super().__init__(name, age, department)
        self.language = language
    
    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.language}")
```

### Usage Example
```python
designer = Designer("Alice", 30, "Design", "Photoshop")
developer = Developer("Bob", 25, "Development", "Python")

designer.display_info()
developer.display_info()
```

---

You can save this content to a `README.md` file in your project directory. It provides a comprehensive guide on the basics of OOP in Python, with examples and explanations for each concept.


## Module Repository:
A module is a file containing Python definitions and statements.
A module is a file containing group of variables, methods, function and classes etc. 
They are executed only the first time the module name is encountered in an import statement.
The file name is the module name with the suffix .py appended. 
Ex:- mymodule.py

### Type of Modules:-
1. User-defined Modules
2. Built-in Modules
          Ex:- array, math, numpy, sys

This repository contains an example of module that perform various tasks. Below is an overview that included:

## Files
### cal.py
```python
def square(myList:list) -> list:
    return [i**2 for i in myList]


def info(**what:dict)->None:
    for key, value in what.items():
        print(f"{key} is {value}")

def add(a : int, b: int) ->int:
    return a+b
``` 
     
### error.py
This file handles errors:
```python
def zeroError(a : int) -> str:
    if (a == 0):
        raise "Zero Division Error"
    else:
      return "You nailed it!"
```      
### msg.py

This file contains a multiline message:
```python
message: str: Welcome message with a Python programming theme.
line: str: A simple line.
```
### main.py

This example demonstrates the usage of functions from the other files:
```python
from msg import message as M,  line as L
from cal import square as s, add as a, info as i
from error import zeroError as e
print(L)
print(M)
print(L)
lt : list = s([1,2,3,4,5,6])
add : int = a(10,5)
dt : dict = i(name="Umer", age = 1)
```
### Example Output
```python
THANK YOU
Welcome to Our
    Python Programming
                        World
Python is not For Innocent People
THANK YOU
{'name': 'Umer', 'age': 16}
THANK YOU
[1, 4, 9, 16, 25, 36]
THANK YOU
15
THANK YOU
You nailed it!
THANK YOU
```
## Package Repository:
 This repository contains a Python package that demonstrates basic usage and organization of a package. ###Step-by-Step Guide: ##Create the Package:

Create a directory named MyPythonPackage. Inside it, create a subdirectory named mypackage. In mypackage, create two files:

init.py: An empty file to mark the directory as a package.

module_inside_package.py: Content of this file should be:

### mypackage/module_inside_package.py
### Example
```python
def multiply(a:int, b:int)->int:
    return a * b
##Create the Main Script:

create a file named main_package.py with the following content:

# main_package.py

# Import the multiply function from mypackage
from mypackage.module_inside_package import multiply

if __name__ == "__main__":
    # Use the imported function
    result = multiply(3, 5)
    print("Result:", result)
```    
### output:
```python
Result: 15
```


        

        
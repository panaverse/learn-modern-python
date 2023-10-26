
# Python Looping and Input Techniques

This guide provides an overview of various looping structures and input methods in Python, emphasizing static type annotations.

## YouTube link
[2 hour live session](https://youtube.com/live/W5KCwG2l3R8)

## Table of Contents
1. [While Loop](#while-loop)
2. [For Loop](#for-loop)
3. [Control Statements](#control-statements)
    - [Break](#break)
    - [Continue](#continue)
    - [Pass](#pass)
4. [Input Function](#input-function)
5. [Command Line Arguments (sys.argv)](#command-line-arguments-sysargv)
6. [Examples](#examples)

---

## While Loop

The `while` loop in Python is used for repeated execution as long as an expression is true.

### Syntax:

```python
while expression:
    # code to be executed
```

### Example:

```python
counter: int = 0
while counter < 5:
    print("Counter is:", counter)
    counter += 1
```

---

## For Loop

The `for` loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects.

### Syntax:

```python
for variable in sequence:
    # code to be executed
```

### Example:

```python
numbers: list = [1, 2, 3, 4, 5]
for num in numbers:
    print("Number is:", num)
```

---

## Control Statements

### Break

The `break` statement is used to exit the loop before it has completed its natural cycle.

#### Example:

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

### Continue

The `continue` statement is used to skip the rest of the code inside the loop for the current iteration only.

#### Example:

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

### Pass

The `pass` statement is a null operation; nothing happens when it executes.

#### Example:

```python
for i in range(5):
    if i == 3:
        pass
    print(i)
```

---

## Input Function

The `input()` function allows for user input.

### Syntax:

```python
variable: str = input("Prompt Message")
```

### Example:

```python
name: str = input("Enter your name: ")
print("Hello,", name)
```

---

## Command Line Arguments (sys.argv)

`sys.argv` is a list in Python, which contains the command-line arguments passed to the script.

### Example:

```python
import sys
arguments: list = sys.argv
print("Script Name:", arguments[0])
print("First Argument:", arguments[1])
```

---

## Examples

You can find various examples in this guide demonstrating how to use while loops, for loops, control statements, the input function, and command line arguments in Python.


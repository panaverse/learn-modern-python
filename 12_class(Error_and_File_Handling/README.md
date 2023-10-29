# Python Error Handling and File Handling Guide

This guide provides an overview of error handling techniques in Python, including creating custom errors and dynamic error handling. It also covers file handling with various access modifiers and reading files of different types such as CSV, PDF, Excel, and audio files.

## YouTube link
[2 hour live session](https://youtube.com/live/v79aciliCkM)

## Table of Contents

- [Error Handling](#error-handling)
  - [Try-Except-Else](#try-except-else)
  - [Multiple Except Blocks](#multiple-except-blocks)
  - [Creating Custom Errors](#creating-custom-errors)
  - [Dynamic Error Handling](#dynamic-error-handling)
- [File Handling with Access Modifiers](#file-handling-with-access-modifiers)
  - [Read Mode (r)](#read-mode-r)
  - [Read and Write Mode (r+)](#read-and-write-mode-r)
  - [Write Mode (w)](#write-mode-w)
  - [Write and Read Mode (w+)](#write-and-read-mode-w)
  - [Append Mode (a)](#append-mode-a)
  - [Append and Read Mode (a+)](#append-and-read-mode-a)
  - [Binary Read Mode (rb)](#binary-read-mode-rb)
- [Reading Files](#reading-files)
  - [Reading CSV Files](#reading-csv-files)
  - [Reading PDF Files](#reading-pdf-files)
  - [Reading Excel Files](#reading-excel-files)
  - [Reading Audio Files](#reading-audio-files)

## Error Handling

### Try-Except-Else

Using `try`, `except`, and `else` blocks allows you to handle errors gracefully and execute code when no errors occur.

```python
def divide(a: float, b: float) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return 0.0
    else:
        print("Division successful")
        return result
```

### Multiple Except Blocks

You can handle different types of exceptions using multiple `except` blocks.

```python
def convert_to_int(value: str) -> int:
    try:
        return int(value)
    except ValueError:
        print("Invalid integer!")
        return 0
    except TypeError:
        print("Value must be a string!")
        return 0
```

### Creating Custom Errors

You can create custom error classes by inheriting from the base `Exception` class.

```python
class NegativeValueError(Exception):
    def __str__(self) -> str:
        return "Value cannot be negative"

def sqrt(value: float) -> float:
    if value < 0:
        raise NegativeValueError()
    return value ** 0.5
```

### Dynamic Error Handling

You can handle errors dynamically by capturing the exception and analyzing it.

```python
def dynamic_error_handling(value: str) -> int:
    try:
        return int(value)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return 0
```

## File Handling with Access Modifiers

### Read Mode (r)

Opens a file for reading.

```python
with open('file.txt', 'r') as f:
    content = f.read()
    print(content)
```

### Read and Write Mode (r+)

Opens a file for reading and writing.

```python
with open('file.txt', 'r+') as f:
    content = f.read()
    print(content)
    f.write("New line")
```

### Write Mode (w)

Opens a file for writing, creates the file if it does not exist, and truncates the file if it exists.

```python
with open('file.txt', 'w') as f:
    f.write("Hello, World!")
```

### Write and Read Mode (w+)

Opens a file for writing and reading.

```python
with open('file.txt', 'w+') as f:
    f.write("Hello, World!")
    f.seek(0)
    content = f.read()
    print(content)
```

### Append Mode (a)

Opens a file for appending, creates the file if it does not exist.

```python
with open('file.txt', 'a') as f:
    f.write("Appending line")
```

### Append and Read Mode (a+)

Opens a file for appending and reading.

```python
with open('file.txt', 'a+') as f:
    f.write("Appending line")
    f.seek(0)
    content = f.read()
    print(content)
```

### Binary Read Mode (rb)

Opens a file in binary read mode.

```python
with open('file.txt', 'rb') as f:
    content = f.read()
    print(content)
```

## Reading Files

### Reading CSV Files

You can use the `csv` module to read CSV files.

```python
import csv

with open('file.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### Reading PDF Files

You can use the `PyPDF2` library to read PDF files.

```python
import PyPDF2

with open('file.pdf', 'rb') as f:
    reader = PyPDF2.PdfFileReader(f)
    text = reader.getPage(0).extractText()
    print(text)
```

### Reading Excel Files

You can use the `openpyxl` library to read Excel files.

```python
import openpyxl

wb = openpyxl.load_workbook('file.xlsx')
sheet = wb.active
cell = sheet['A1']
print(cell.value)
```

### Reading Audio Files

You can use the `pydub` library to read audio files.

```python
from pydub import AudioSegment

audio = AudioSegment.from_file("file.mp3")
print("Channels:", audio.channels)
print("Sample Width:", audio.sample_width)
print("Frame Rate:", audio.frame_rate)
print("Frame Width:", audio.frame_width)
print("Length (ms):", len(audio))
print("Frame Count:", audio.frame_count())
```

Remember to install the necessary libraries before running the code examples.

```bash
pip install PyPDF2 openpyxl pydub
```

This README provides a comprehensive guide on various error handling and file handling techniques in Python, along with examples of reading different file types. Feel free to modify and extend it as per your project's requirements.
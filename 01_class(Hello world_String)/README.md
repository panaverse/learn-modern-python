# Project Setup Guide

This guide explains how to set up the development environment using Anaconda, Visual Studio Code (VS Code), and Python.

## YouTube Tutorial Link 
[2 hours live session](https://www.youtube.com/watch?v=rwDHhx76MMg)

## Prerequisites

- [Anaconda](https://www.anaconda.com/products/individual#Downloads)
- [VS Code](https://code.visualstudio.com/Download)

---

## Table of Contents

1. [Running a "Hello World" Program](#running-a-hello-world-program)
2. [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)

---

## Running a "Hello World" Program

You can run a simple "Hello World" program to ensure that your Python setup is working as expected.

### Using Anaconda Prompt on Windows

1. Open Anaconda prompt
2. Run the following Python command:

    ```bash
    python -c "print('Hello world')"
    ```

### Using VS Code (.py file)

1. Open VS Code and create a new Python file called `class1.py`.
2. Write the following Python code:

    ```python
    print("Hello world")
    ```

3. Install the Python extension for VS Code if you haven't done so.
4. Click on the Run button to execute the code.

### Using VS Code (.ipynb file)

1. Open VS Code and create a new Jupyter Notebook called `class1.ipynb`.
2. Insert the following Python code into a new cell:

    ```python
    print("Hello world")
    ```

3. Click on the Run button to execute the cell.

---

## Setting Up a Virtual Environment

### Creating a New Environment

1. Run the following command to create a new Conda environment:

    ```bash
    conda create -n <env_name> python==3.12 -y
    # Example: conda create -n python12 python==3.12 -y
    ```

2. Activate your newly created environment:

    ```bash
    conda activate <env_name>
    # Example: conda activate python12
    ```

### Installing Required Packages

1. Create a `requirements.txt` file with the following content:

    ```
    mypy
    ```

2. Run the following command to install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Selecting the Environment in VS Code

1. Open `class1.py` in VS Code.
2. Select your virtual environment as shown below:

    ![Alt text](image-2.png)

    ![Alt text](image-1.png)

### Selecting the Environment in Jupyter Notebook

1. Open `class1.ipynb` in Jupyter Notebook.
2. Select your virtual environment as shown below:

   ![Alt text](<Screenshot 2023-10-16 at 10.34.08 PM.png>)

    ![Alt text](image-1.png)




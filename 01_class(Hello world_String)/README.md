# Installation
* Anaconda
    * https://www.anaconda.com/download
* vs code

# Hello world
* windows->Anaconda prompt->python
```
print("Hello world")
```

* open VScode -> `class1.py`
```
print("Hello world")
```
    * install python extension
    * click on run button

* open VScode -> `class1.ipynb`
```
print("Hello world")
```
    * click on run button

# Create Virtual Envornment 
1. `conda create -n <env_name> python==3.12 -y`
    * I have used `conda create -n python12 python==3.12 -y`
2. `conda activate python12`
3. create `requirements.txt` file
```
mypy
```
4. `pip install -r requirements.txt`
5. select virtual env in **vscode**
    * open **class1.py**
    ![Alt text](image-1.png)
    




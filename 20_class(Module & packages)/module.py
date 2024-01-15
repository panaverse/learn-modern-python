# MODULE:
# In Python we are able to write a long program and save as a module.
# This is known as creating a script. We are able to import modules 
# across modulesand into the Python interpreter. This negates the 
# need to keep repeating ourselves.
# DRY!....Don't repeat yourself
# '''
# import ModuleExample
# ModuleExample.add(4,5.5)

# #We can import a module by renaming it as follows:
# # import module by renaming it

# import ModuleExample as m
# print("The addition is ",m.add(4,5.5))

# #Python import statement
# # import statement example
# # to import standard module math
# import math
# print("The value of pi is", math.pi)

# #Python from...import statement
# # import only pi from math module
# from math import pi
# print("The value of pi is", pi)

# Example:
 
# Python/cal.py

def square(myList:list) -> list:
    return [i**2 for i in myList]


def info(**what:dict)->None:
    for key, value in what.items():
        print(f"{key} is {value}")

def add(a : int, b: int) ->int:
    return a+b

#  Python/error.py
def zeroError(a : int) -> str:
    if (a == 0):
        raise "Zero Division Error"
    else:
      return "You nailed it!"
    
 #  Python/msg.py

message : str = """
Welcome to Our
    Python Programming
                        World
Python is not For Innocent People
"""
line : str = "THANK YOU"
 
#  Python/main.py

from msg import message as M,  line as L
from cal import square as s, add as a, info as i
from error import zeroError as e
print(L)
print(M)
print(L)
lt : list = s([1,2,3,4,5,6])
add : int = a(10,5)
dt : dict = i(name="Umer", age = 16)
print(lt)
print(L)
print(dt)
print(L)
print(add)
print(L)
print(e(0))
print(L)

print("-------------------------------------------------------")


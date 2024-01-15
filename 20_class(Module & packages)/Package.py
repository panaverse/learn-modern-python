#PACKAGE:
#A package can have one or more modules which means, a package is collection of modules and packages. 
# A package can contain packages. 
# Package is nothing but a Directory/Folder
# It MUST contain a special file called __init__.py. 
# __init__.py file can be empty, it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.


# Syntax:- import packageName.moduleName
# Syntax:- import packageName.subPackageName.moduleName


# How to Access Variable, Function, Method, Class etc. ?

# Syntax:- packageName.moduleName.functionName()
# Syntax:- packageName.subPackageName.moduleName.functionName()

# Syntax:- from packageName import moduleName
# Syntax:- from packageName.subPackageName import moduleName


# if a package’s __init__.py code defines a list named __all__, it is taken to be the list of module names that should be imported when from package import * is encountered. 
# __all__ = []

import sys

print("line1")
print("line2")

print(type(sys.argv)) 

if sys.argv[1] == '-g':
    print("I will install this package on globally in your system!")

print(sys.argv) # iterative data type list[str] 0=filename **value user define
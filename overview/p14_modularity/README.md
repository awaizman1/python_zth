# Function
The smallest granularity of reusable code
```python
# syntax
def functionname( args ):
    "function_docstring"
    function_suite
    return [expression]
```
```python
# example
def foo(x, y, z):
    return x + y + z
```
# Module
A collection of functions and source code in a single ***.py*** file.  
[modules](https://docs.python.org/3/tutorial/modules.html#modules)  
 ### fibo.py
![](/images/p14-1.png)
## Reusing a module
A module can be either imported by another module or run directly by the interactive interpreter.
```python
# greet.py module

def print_greeting():
    print('have a nice day')

print_greeting()
```
#### Importing a module
```python
# my_module.py module

import greet

greet.print_greeting()
```
#### Running a module from interactive interpreter
```cmd
$ python greet.py
have a nice day
```
#### Distinguish between import and running as a script
module's [\_\_name\_\_ ](
```python
# greet.py module - fixed!

def print_greeting():
    print('have a nice day')

if __name__=="__main__":
    print_greeting()
```
# Package
A collection of modules (sub-modules) and other packages (sub-packages).
![](/images/p14-2.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg3MjIxMjgyMCw2NTY2ODM3NywtMjAzMz
MxNzE0NCwxNDQ0NDc3NTY3LDEwMTI5ODM1OTZdfQ==
-->
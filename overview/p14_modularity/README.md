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
### Importing a module
```python
# my_module.py module

import greet

greet.print_greeting()
```

# Package
A collection of modules (sub-modules) and other packages (sub-packages).
![](/images/p14-2.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzg4MDM1MTQ1LDY1NjY4Mzc3LC0yMDMzMz
E3MTQ0LDE0NDQ0Nzc1NjcsMTAxMjk4MzU5Nl19
-->
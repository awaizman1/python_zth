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
A module can be either imported by another module or run directly by the interpreter
# Package
A collection of modules (sub-modules) and other packages (sub-packages).
![](/images/p14-2.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMDk4NDgwMTYsNjU2NjgzNzcsLTIwMz
MzMTcxNDQsMTQ0NDQ3NzU2NywxMDEyOTgzNTk2XX0=
-->
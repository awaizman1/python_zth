# Comments and docstring
Use docstrings and comments for d
# docstrings
- Focused on what!
- Targeting your consumers.
- Useful with [help](https://docs.python.org/3/library/functions.html#help) builtin function.
- Document only public package / module / class / method / function, not private ones!   

> package docstrings is placed in package's ***__init__.py*** file (will be discussed later)

The code below shows module, class, method and function docstrings:
```python
"""
A very basic calculator
"""

def get_default_calculator():
    """
    Gets the default calculator
    """
    
	return Calculator(True)

class Calculator:
    """ Provides basic calculator operations. """
	
    def __init__(self, print_to_console):
	    """
	    Initializes the calculator
	    
	    :param print_to_console: controls whether to print all operations
	    """

		self._print_to_console = print_to_console

    def add(self, a, b):
        """
        Adds 2 numbers.
        
        :param a: first arg
        :param b: second arg
        :return: a + b
        """

        if self._print_to_console:
            print(f"adding {a} and {b}")
        
        return a + b
```
Now we get informative description of our module:
```python
>>> import calculator
>>> help(calculator)
Help on module calculator:
NAME
    calculator - A very basic calculator
CLASSES
    builtins.object
        Calculator
    
    class Calculator(builtins.object)
     |  Calculator(print_to_console)
     |  
     |  Provides basic calculator operations.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, print_to_console)
     |      Initializes the calculator
     |      
     |      :param print_to_console: controls whether to print all operations
     |  
     |  add(a, b)
     |      Adds 2 numbers.
     |      
     |      :param a: first arg
     |      :param b: second arg
     |      :return: a + b
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
FUNCTIONS
    get_default_calculator()
        Gets the default calculator
FILE
    /Users/assaf/calculator.py
```
# Comments
- Focused on why and how!
- Targeting you and fellow developers.
-  Document public and private package / module / class / method / function as needed.
```python
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg2NjMzNTA3NiwtMjc3OTQwNTEzLC05Mz
M5ODExNjNdfQ==
-->
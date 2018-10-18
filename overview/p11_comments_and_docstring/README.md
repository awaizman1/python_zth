# Comments and docstring
Use docstrings and comments for documenting your code.
# docstrings
- Focused on what!
- Targeting your consumers.
- Useful with [help](https://docs.python.org/3/library/functions.html#help) builtin function.
- Document only public package / module / class / method / function, not private ones!   
- There are tools for creating web / pdf / etc. documentation from docstrings (i.e. [sphinx](http://www.sphinx-doc.org/en/master/)).

> package docstrings is placed in package's ***__\__init__\__.py*** file (will be discussed later)

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
# create a list of ints (single line comment)
l = [1, 2, 3]

# create a list of ints (comments block)
# list on index i will hold i + 1
# ...
l = [1, 2, 3]

l = [1, 2, 3]  # create a list of lines (inline comment)
```
# Advanced
How does [help](https://docs.python.org/3/library/functions.html#help) works? where are docstrings being stored?
everything in python is an object, play around with some documented code using [dir](https://docs.python.org/3/library/functions.html#dir) and check **\_\_doc__** (dunder doc) attribute.  

docstrings format can be much more than plain text. For example, using [reStructuredText](http://docutils.sourceforge.net/rst.html) format allows parsers and generators to create rich, beautiful docs.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMxMDE0NDI1NywtNjAyNDYwNjUzLC05NT
QzNTc0NjMsMTgxNjI2NDkwNywtMjc3OTQwNTEzLC05MzM5ODEx
NjNdfQ==
-->

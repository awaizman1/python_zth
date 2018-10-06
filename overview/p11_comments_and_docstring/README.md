# Comments and docstring
Use docstring to document public package / module / class / method / function. docstring should focus on what and are mainly for your users.
Use comments to explain the way. comments are for you and fellow developers.
# docstrings
- Focuses on what!
- Targeting your consumers.
- Useful with [help](https://docs.python.org/3/library/functions.html#help) builtin function.
- Document only public package / module / class / method / function, not private ones!   

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
	
    def __init__(print_to_console):
	    """
	    Initializes the calculator
	    
	    :param print_to_console: controls whether to print all operations
	    """

		self._print_to_console = print_to_console

    def add(a, b):
        """
        Adds 2 numbers.
        
        :param a: first arg
        :param b: second arg
        :return: a + b
        """

        if self._print_to_console:
            print(f"adding {a} and {b}"})
        
        return a + b
```
```python
help(calculator
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI3Nzk0MDUxMywtOTMzOTgxMTYzXX0=
-->
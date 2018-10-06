# Comments and docstring
Use docstring to document public package / module / class / method / function. docstring should focus on what and are mainly for your users.
Use comments to explain the way. comments are for you and fellow developers.
# docstrings
```python
""" A basic calculator

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
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIzOTM5NDE4NCwtOTMzOTgxMTYzXX0=
-->
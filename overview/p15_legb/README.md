# Variable Scoping Rules
Whenever the interpreter accesses a variable (named reference), it follows the scoping rules:

 1. **Local** - inside the current function.
 2. **Enclosing** - any enclosing function.
 3. **Global** - module top level
 4. **Built-in** - provided by the `builtins` module

> if, for, while, with blocks doesn't add new scope

![](/images/p15-1.png)
## [global](https://docs.python.org/3/reference/simple_stmts.html#global) keyword
The [`global`](https://docs.python.org/3/reference/simple_stmts.html#global) statement causes the listed identifiers to be interpreted as globals.
```python
# legb.py module

count = 0

def print_count():
    print(count)  # L-->E-->*G*

def set_count(value):
    count = value # *L*
``` 
```python
>>> from legb import print_count, set_count

>>> set_count(5)
>>> print_count()
0
```
#### using the `global` keyword
```python
# legb.py module

count = 0

def print_count():
    print(count)  # L-->E-->*G*

def set_count(value):
	global count  # now count is the global one
    count = value  # L-->E-->*G*
``` 
```python
>>> from legb import print_count, set_count

>>> set_count(5)
>>> print_count()
5
```
## [nonlocal](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) keyword
The [`nonlocal`](https://docs.python.org/3/reference/simple_stmts.html#nonlocal) statement causes the listed identifiers to refer to previously bound variables in the nearest enclosing scope excluding globals.
```python
# legb.py module

def outer():
    a_var = 'enclosed value'

    def inner():
        a_var = 'local value'
        print("within inner: " + a_var)
    
    print("before inner call: " + a_var)
    inner()
    print("after inner call: " + a_var)
```
```python
>>> from legb import outer

>>> outer()
before inner call: enclosed value
within inner: local value
after inner call: enclosed value
```
#### using the `nonlocal` keyword
```python
# legb.py module

def outer():
    a_var = 'enclosed value'

    def inner():
	    nonlocal a_var
        a_var = 'local value'
        print("within inner: " + a_var)
    
    print("before inner call: " + a_var)
    inner()
    print("after inner call: " + a_var)
``` 
```python
>>> from legb import outer

>>> outer()
before inner call: enclosed value
within inner: local value
after inner call: local value
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3Njk2MzI2MjIsLTE1MDI1NTE1NTIsLT
EzMjY3NzEyODIsMjEyMTczMDI1N119
-->
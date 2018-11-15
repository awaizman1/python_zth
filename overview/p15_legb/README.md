# Variable Scoping Rules
Whenever the interpreter accesses a variable (named reference), it follows the scoping rules:

 1. **Local** - inside the current function.
 2. **Enclosing** - any enclosing function.
 3. **Global** - module top level
 4. **Built-in** - provided by the `builtins` module

> if, for, while, with blocks doesn't add new scope
![](/images/p15-1.png)
```python
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
```python
count = 0

def print_count():
    print(count)

def set_count(value):
	global count
    count = value . #
``` 
```python
>>> from legb import print_count, set_count

>>> set_count(5)
>>> print_count()
5
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbODkyNDAyMTA5LC0xMzI2NzcxMjgyLDIxMj
E3MzAyNTddfQ==
-->
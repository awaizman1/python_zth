# Tuple
Immutable sequence of objects.
## tuple literals
```python
>>> # empty tuple
>>> t = ()

>>> # single element tuple
>>> t = (1,)
>>> t = 1,

>>> # tuple of hetrogenous items
>>> t = (1, "two", 3.0)
>>> t = 1, "two", 3.0
```
## tuple unpacking
```python
>>> def foo():
...     return 1, 2, 3

>>> a = foo()
>>> a
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgyNjEyNjgwOSwxMDA3Mjc5Njc5XX0=
-->
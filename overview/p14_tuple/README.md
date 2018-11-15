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
>>> # returning multiple objects from function is done using tuple
>>> def foo():
...     return 1, 2, 3

>>> a = foo()
>>> a
(1, 2, 3)
>>> # tuple unpacking
>>> a, b, c = foo()
>>> a
1
>>> b
2
>>> c
3
>>> a, _, c = foo()
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc0MzAxMzI0NSwxMDA3Mjc5Njc5XX0=
-->
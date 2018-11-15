# Tuple
Immutable sequence of objects.
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple) is a `sequence` so all sequence operations apply to it (in, [], iterating, slicing, ...)
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
>>> # use _ for unused variables (IDEs aware of this convension)
>>> a, _, c = foo()
```
# Named tuple
a way of creating tuple subclass which provides:
[namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)
 - own type
 - accessible fields
 - docstring
 - helpful \_\_repr\_\_
 
 ```python
>>> Point = namedtuple('Point', field_names=('x', 'y'), defaults=(0, 0))
>>> p1 = Point()
>>> p1

 ```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjkyNTkzMjc4LDEzODkzODkwMzksLTE5MT
U0OTkxNjEsMTAwNzI3OTY3OV19
-->
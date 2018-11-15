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
>>> # create new namedtuple
>>> Point = namedtuple('Point', field_names=('x', 'y'), defaults=(0, 0))

>>> # namedtuple defaults
>>> Point()
Point(x=0, y=0)

>>> # instantiate with named args
>>> Point(x=1, y=5)
Point(x=1, y=5)

>>> # instantiate with positional args
>>> Point(1, 2)
Point(x=1, y=2)

>>> # field access
>>> p = Point(1,2)
>>> p.x
1
 ```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMyODIzNjM5NCwxMzg5Mzg5MDM5LC0xOT
E1NDk5MTYxLDEwMDcyNzk2NzldfQ==
-->
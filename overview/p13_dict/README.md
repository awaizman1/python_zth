# Dict
mutable mapping of keys to values.
[Mapping types](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
[dict](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
## Dict literal
```python
>>> # empty dict
>>> d = {}

>>> # dict of homogenous keys and values (str --> int)
>>> d = {'one': 1, 'two': 2}

>>> # dict of hetrogenous keys and values
>>> d = {'one': 1, 2: 'two'}
```
## Dict operations
```python
>>> d = {1: 'one', 2: 'two', 3: 'three'}
>>> # access item by key
>>> d[3]
'three'
>>> # modify item at key
>>> d[3] = 'THREE'
>>> d
{1: 'one', 2: 'two', 3: 'THREE'}
>>> # add new item at key (creates new entry)
>>> d[4] = 'four'
>>> d
{1: 'one', 2: 'two', 3: 'THREE', 4: 'four'}
>>> # remove item at key
>>> del d[4]
>>> d
{1: 'one', 2: 'two', 3: 'THREE'}
>>> len(d)
3
>>> 2 in d
True
>>> 
```
## Iterating dict
```python
>>> d = {1: 'one', 2: 'two', 3: 'three'} 
>>> # iterate over keys
>>> for k in d:
>>>     print(d[k])

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI0MzAyMTg1MiwtODI4NzQ3Nzk1LDIwMT
c3NDgyMzVdfQ==
-->
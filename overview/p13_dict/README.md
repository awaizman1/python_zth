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
one
two
three
>>> # iterate over key, value pairs
>>> for k, v in d.items():
>>>     print(f"{k} --> {v}")
1 --> one
2 --> two
3 --> three
>>> # iterate over values
>>> for v in d.values():
>>>     print(v)
one
two
three
```
## Other useful methods
Instead of:
```python
if 'key' in d:
 return d['key']
else:
 d['key'] = value
 return d['key']
```
write:
```python
return d.setdefault('key', value)
```
Instead of:
```python
if 'key' in cache:
 return cache['key']
else:
 return 'not found'
```
write:
```python
return cache.get('key', 'not found')
```
## Keys immutability
dict keys must be immutable (i.e. list can't be dict key).
In more details, keys must be [hashable](https://docs.python.org/3/glossary.html#term-hashable).
![](/images/p13-1.png)
## dict comprehension
Similarly to [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#tut-listcomps), dict comprehensions are also supported:
```python
>>> {x: x**2 for x in (2, 4, 6)}
{2: 4, 4: 16, 6: 36}
```

### Time for task:
 - perform ***task.py***
 - test yourself by running ***test_task.py***
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzM5MTQxODg5LDczMjYxMTA5LC0xMjY4OD
A0NDM4LC0xODkxMDg4MzgzLC04Mjg3NDc3OTUsMjAxNzc0ODIz
NV19
-->

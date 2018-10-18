# List
***Mutable*** sequences of objects
```python
>>> # empty list
>>> l = []

>>> # list of hetrogeneous items
>>> l = [1, "two", 3.0]
>>>
```
## List is a sequence, so...
```python
>>> # concatanation
>>> [1, 2] + [3, 4]
[1, 2, 3, 4]

>>> # repetition
>>> [1, 2] * 2
[1, 2, 1, 2]

>>> # membership testing
>>> 3 in [1, 2, 4]
False

>>> # other sequence methods
>>> len([1, 2])
2
>>> [1, 2, 1].count(1)
2
>>> [1, 2].index(2)
1

>>> # list is a mutable sequence
>>> l = [1, 2, 3]
>>> l[1:] = [4, 5, 6]
>>> l
[1, 4, 5, 6]
>>> del(l[1])
>>> l
[1, 5, 6]

>>> # coping a list (not the reference!)
>>> l = [1, 2, 3]
>>> l2 = l[:]
>>> id(l) == id(l2)
False 
>>> l2 = l.copy()
>>> l2 = list(l)

>>> # 
>>> l[:] = [4, 5, 6]
>>> l[:] = []
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzOTgxNTk3NzgsLTkxNzQzODQzNywxND
kxNzEyNDkzLDEwMjM1ODc1NDhdfQ==
-->
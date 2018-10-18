# List
***Mutable*** sequences of objects
[list](https://docs.python.org/3.7/tutorial/datastructures.html)
## List literal
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

>>> # emptying a list (not assigning new empty list to the reference!)
>>> l[:] = []
```
### Comparing lists (or any other sequence)
- comparison uses lexicographical ordering
- equality is deep element-wise equality
[comparing-sequences](https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types)
```python
[1, 2, 3] < [1, 2, 4]

[1, 2] < [1, 2, -1]

[1, 2] == [1, 2]

[1, 2] == [1.0, 2.0]
```
## Slicing (of list or any other sequence)
![](/images/p12-slice.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5Nzg3NTk4MSwtMTg5MDI0ODk3MywxMj
k2MzQ1NDI1LC0xNzgwMDI1NTM2LC05MTc0Mzg0MzcsMTQ5MTcx
MjQ5MywxMDIzNTg3NTQ4XX0=
-->
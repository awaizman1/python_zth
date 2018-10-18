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
```python
sequence[start:stop:step]
```
* ***start [default = 0]*** - the beginning index of the slice (including this index)
* ***end [default = len(sequence)]*** - the ending index of the slice (excluding this index)
* ***step [default = 1]*** - the amount by which the index increases
```python
>>> a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
>>> a[2:5]
['baz', 'qux', 'quux']

>>> a[4:]
['quux', 'corge']

>>> a[:2]
['foo', 'bar']

>>> a[:]
['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

>>> a[::2]
['foo', 'baz', 'quux']

>>> # reverse
>>> a[::-1]
['corge', 'quux', 'qux', 'baz', 'bar', 'foo']

>>> # last 2 items
>>> a[-2:]
['quux', 'corge']

>>> # everything except the last two items
>>> a[:,-2]
['foo', 'bar', 'baz', 'qux']
```
## List comprehensions
A concise way to create lists.
* readable
* expressive
* effective
* great for ***map / filter*** operations
[list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
### Syntax
```python
[ expression for-clause [for-clause | if-clause]* ]
```
### Examples
#### Simple comprehension
```python
squares = []
for x in [1, 2, 3]:
	squares.append(x**2)
```
```python
[x**2 for x in [1, 2, 3]]
```
#### With filtering
```python
even_squares = []
for x in range(10):
	if x % 2:
		even_squares.append[x**2]
```
```python
[x**2 for x in range(10) if x % 2]
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY5NjExNTM5MywxODk1MTEyNTAyLDE2MT
Y0MzYxNCwtMTk3ODc1OTgxXX0=
-->
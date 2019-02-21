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
> If a negative stride is specified and the start or end indices are omitted,
they default to ***-1*** and ***-1\*len(sequence) - 1*** respectively.

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
```

```python
>>> # reverse
>>> a[::-1]
['corge', 'quux', 'qux', 'baz', 'bar', 'foo']

>>> # last 2 items
>>> a[-2:]
['quux', 'corge']

>>> # everything except the last two items
>>> a[:-2]
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
>>> [x**2 for x in [1, 2, 3]]
[1, 4, 9]
```
#### With filtering
```python
even_squares = []
for x in range(10):
	if x % 2:
		even_squares.append[x**2]
```
```python
>>> [x**2 for x in range(10) if x % 2]
[1, 9, 25, 49, 81]
```
#### Combining several sequences
```python
>>> [f"({a}x{b})" for a in range(3) for b in range(3)]
['(0x0)', '(0x1)', '(0x2)', '(1x0)', '(1x1)', '(1x2)', '(2x0)', '(2x1)', '(2x2)']
```
#### Combining several sequences and filters
```python
[send_message(host, port) for host in hosts if host not in black_list for port in get_ports(host)]

[send_message(host, port) 
for host in hosts 
if host not in black_list 
for port in get_ports(host)]

```
### Nested comprehension
Each element in the comprehension can be a comprehension...
```python
seq_up_to = []
for i in range(1, 5):
	seq_up_to_i = []
	for j in range(i):
		seq_up_to_i.append(j)
		
	seq_up_to += seq_up_to_i
```
```python
>>> [[x for x in range(i)] for i in range(1, 5)]
[[0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
```
### Time for task:
 - perform ***task.py***
 - test yourself by running ***test_task.py***
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzMDU0NDkyMzcsOTAyMzQyMjQwLC0xMD
Y2NTA4NDk5LC0xNDQ4ODUyOTI1LDE2OTYxMTUzOTMsMTg5NTEx
MjUwMiwxNjE2NDM2MTQsLTE5Nzg3NTk4MV19
-->

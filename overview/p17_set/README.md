# Set
Unordered collection of unique, immutable objects.
## Set literals
```python
# empty set
empty_set = set() . # not {} since it resevered for dict...

# set of objects
int_set = {1, 4, 2, 7}

# set of hetrogenous objects
hetro_set = {1, False, 4.3}
```
## Set algebra
[set](https://docs.python.org/3.7/library/stdtypes.html?highlight=set#set)
```python
a = {1, 2, 3}
b = {3, 4, 5}
```
### Union
![union](/images/p17-union.png)
```python
>>> a.union(b)  # or a | b
set([1, 2, 3 ,4 ,5])
```
### Intersection
![intersect](/images/p17-intersect.png)
```python
>>> a.intersection(b)  # or a & b
set([3])
```
### Difference
![diff](/images/p17-difference.png)
```python
>>> a.difference(b)  # or a - b
set([1, 2])
```
### Symmetric difference
![sym-diff](/images/p17-symmetric-diff.png)
```python
>>> a.symmetric_difference(b)  # or a ^ b
set([1, 2, 4, 5)
```
### Other useful operations
```isdisjoint```, ```issubset```, ```issuperset```
## Time for task:
 - perform ***task.py***
 - test yourself by running ***test_task.py***
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM2MDg1NTkzMywtNjY1ODQwOTQzLC0xOT
M0MjA0NDgzXX0=
-->
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
```python
a = {1, 2, 3}
b = {3, 4, 5}
```
### Union
![unioun](/images/p17-union.png)
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
[diff](/images/p17-difference.png)
```python
>>> a.difference(b)  # or a - b
set([1, 2])
```
### Symmetric difference
[diff](/images/p17-symmetric-difference.png)
```python
>>> a.symmetric_difference(b)  # or a ^ b
set([1, 2, 4, 5)
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk0NzAzMTMxLC0xOTM0MjA0NDgzXX0=
-->
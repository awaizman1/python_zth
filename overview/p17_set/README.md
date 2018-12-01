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
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDc2NzU5MDY1LC0xOTM0MjA0NDgzXX0=
-->
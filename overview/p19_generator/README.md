# Generator
Generators are functions that can be paused and resumed on the fly, returning an object that can be iterated over.
A generator is lazy evaluated - produces one item at a time and only when asked.

 - Can model infinite sequences (streams)
 - Memory efficient
 - Composable into pipelines
 - Can maintain state and control flow

> Every generator is an iterator.

## Creating a generator
Regular function with ```yield``` statement.
```python
def count_to_2():
	yield 1
	yield 2
```
```python

>>>  g = count_to_2()
>>> next(g)
1
>>> next(g)
2
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
```python
>>> for i in count_to_2():
... 	print(i)
1
2
```
## Stateful generator
```python
def count():
	num = 0
	while True:
		yield num
		num += 1
```
```python
>>> for i in count():
... 	print(i)
0
1
2
3
4, 5, 6, ...
```
> What need to happen upon yield so that this magic will work?
>
## Pipelines
Generators can be combined into pipelines for natural stream processing.
```python
def repeat(element, 
```
## Generator expression
Similar to list comprehension, one can create generators
```python
g = (x**2 for x in range(1000) if x % 2 == 0)

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1NjEyNjU3NDgsMTgyMzA0NDg2LDE5OD
c3MTgzMywxMDAxMDM4MzY2XX0=
-->
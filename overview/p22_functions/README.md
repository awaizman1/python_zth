
# Function
The keyword [`def`](https://docs.python.org/3/reference/compound_stmts.html#def) introduces a function _definition_.
```python
def foo(a, b, c):
	"""
	My docstring
	"""
	
	return (a + b) / c
```
### Calling ```foo``` with positional arguments
```python
foo(1, 2, 3)  # a = 1, b = 2, c = 3
```
### Calling ```foo``` with keyword arguments
```python
foo(b=2, a=1, c=3)  # any order for keyword args
```
```python
foo(1, b=2, c=3)  # mixing positional and keyword args
```
## Default args
```python
def connect(host, port=1234):
	...
```

> **Be careful when using mutable objects as default args!**
> Default args are evaluated only once - at the point of function definition in the _defining_ scope.
```python
def make_pair(a, b, pair=[]):
	
	pair.append(a)
	pair.append(b)
	
	return pair 
```
```python
>>> make_pair(1, 2)
[1, 2]
>>> make_pair(3, 4)
[1, 2, 3, 4]
```
## Arbitrary argument list
Arguments will be wrapped up in a tuple.
```python
def sum(initial, *args):

	for arg in args:
		initial += arg
	
	return initial	
```
```python
>>> sum(0, 1, 2, 3)
6
```
### Keyworded arbitrary argument list
```python
def print_info(**kwargs):
	for k, v in kwargs.items():
		print(k, ' --> ', v)
```
```python
>>> print_info(first_name='jhon', last_name='doe', age='21')
first_name --> jhon
last_name --> doe
age --> 21
```
> Written with [StackEdit](https://stackedit.io/).

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk2Mjg5MjcwMiwtMjEzNzY1MjIxOCwtMT
AyODQ1MDEyNSwxMjA1MDI3NjE3LDQ1NzEwNjg1XX0=
-->
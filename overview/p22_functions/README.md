
# Functions
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

> **The choice whether a passed arg is positional / keyword arg is made at the caller side!**
### Function is an object!
```python
>>> foo
<function foo at 0x103cff620>
>>> dir(foo)
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```
## Default args
```python
def connect(host, port=1234):
	...
```

> **Be careful when using mutable objects as default args!**
> Default args are evaluated only once - at the point of function definition in the _defining_ scope.
```python
def append_to(element, to=[]):
	
	to.append(element)
	
	return to
```
```python
>>> append_to(1)
[1]
>>> append_to(2)
[1, 2]
```
### Handling mutable default arguments
```python
def append_to(element, to=None):

	to = [] if to is None else to
	to.append(element)
	return to
```
## Arbitrary argument list
[arbitrary arg lists](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists)
#### Ever wondered how ```print``` works?
```python
>>> print(1)
1
>>> print(1, 2)
1 2
>>> print(1, 2, 3)
1 2 3
```
#### Use the ```*args``` in function definition:
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
#### Ever wondered how ```dict``` works?
```python
>>> dict(name='jhon', age=21)
{'name': 'jhon', 'age': 21}
```
#### Use the ```**kwargs``` in function definition:
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
## Unpacking arguments lists
Sometimes the arguments to a function already exist in a list/tuple/dict.
```python
endpoint=('127.0.0.1', 80)
endpoint_as_dict={'host': '127.0.0.1', 'port': 80} 

connect(*endpoint)  # instead of connect(endpoint[0], endpoint[1])

connect(**endpoint)  # instead of connect(endpoint['host'], endpoint['port'])
```
## Inner / nested / local functions
In python you can define functions within functions:
```python
def foo(a_vec, b_vec, c_vec):
	
	def dotprod(a, b):
		return sum(pair[0] * pair[1] for pair in zip(a, b))
	
	print("a * b is bigger then b * c" 
		  if dotprod(a_vec, b_vec) > dotprod(b_vec, c_vec) else
		  "a * b is bigger then b * c")
```

 - Inner function is not accessible from outside the enclosing function.
 - Inner function object is created per run (and only when running) of the enclosing function.
 - LEGB rules applied to inner functions.
## Closure
A function object that remembers values in enclosing scopes even if they are not present in memory.
```python
def make_power(p):
	
	message = f"pow by {p}"
	
	def power(x):
		print(message)
		ret = 1
		for i in range(p):
			ret *= x
		
		return ret
	
	return power
```
```python
>>> p2 = make_power(2)
>>> p3 = make_power(3)
>>> p2(5)
pow by 2
25
>>> p3(5)
pow by 3
125
```
#### You can inspect the captured values using [```__closure__```](https://docs.python.org/3/reference/datamodel.html#index-34):
```python
>>> p2.__closure__
(<cell at 0x103ce2bb8: str object at 0x103de5530>, <cell at 0x103ce2d38: int object at 0x103a37c70>)
```

> Written with [StackEdit](https://stackedit.io/).

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI3MTIxMjAzLDEyMDI3MTQ0ODIsLTIwNz
c0NjI0MzgsLTc5ODg3NDQ1MiwxMzUxNzQxMjA2LC0xMDM3MTA0
NjkzLC0xMzIyNzI2OTgwLC04MDIzMDI1NDEsLTEwOTAyMTAzOT
AsLTIxMzc2NTIyMTgsLTEwMjg0NTAxMjUsMTIwNTAyNzYxNyw0
NTcxMDY4NV19
-->
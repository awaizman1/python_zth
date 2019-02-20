
# Callables
An object which can be called like a function.
```python
# a function is a callable
def foo():
	print("foo")

foo()
```
```python
# a class is a callable
class A:
	def __init__(self):
		print("A init")

A()
```
## Creating callable objects
Any object which has the [```__call__```](https://docs.python.org/3/reference/datamodel.html#object.__call__) attribute is callable.

> So... this means functions and classes has the ```__call__``` attribute!
```python

```python
class A():
	def __init__(self):
		self.count = 0
	
	def __call__():
		self.count += 1
		print(f"They called me {self.count} times")
```
```python
>>> a = A()
>>> a()
They called me 1 times
>>> a()
They called me 2 times
```

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYxODQyNTQ1OV19
-->
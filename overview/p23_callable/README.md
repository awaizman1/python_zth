
# Callables
An object which can be called like a function.
```python
# a function is a callable (recall a function is an object)
def foo():
	print("hi from foo")

foo()
```
```python
# a class is a callable
class A:
	def __init__(self):
		print("hi from A init")

A()
```
## Creating callable objects
Any object which has the [```__call__```](https://docs.python.org/3/reference/datamodel.html#object.__call__) attribute is callable.

> So... this means functions and classes has the ```__call__``` attribute!
```python
>>> foo()
hi from foo
>>> foo.__call__()  # never invoke __call__ directly
hi from foo
>>> a = A()
hi from A init
a = A.__call__()
hi from A init
```
### Making your object callable
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
### Test whether an object is callable
[```callable```](https://docs.python.org/3/library/functions.html#callable)
```python
>>> callable(A)
True
>>> callable(5)
False
```

## Lambdas
A simple way to create anonymous callables / functions.

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbODc5MjIwMDk0LC0xNzk3ODU3MjYzXX0=
-->
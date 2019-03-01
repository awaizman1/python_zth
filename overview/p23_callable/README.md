
# Callables
An object which can be called like a function.
#### a function is a callable (recall a function is an object):
```python
def foo():
    print("hi from foo")

foo()
```
#### a class is a callable:
```python
class A:
    def __init__(self):
        print("hi from A init")

A()
```
#### a lambda is a callable:
```python
add = lambda x, y: x + y

add(1, 2)
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
[lambda](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)

 - lambdas are anonymous (not bounded to a name)
 - limited to single expression body
 - can reference variables from the containing scope
 - cannot have docstring

#### Syntax:
```python
lambda [arguments]: expression
```
The expression:
```python
add = lambda x, y: x + y
```
is equivalent to:
```python
def add(x, y):
	return x + y
```
#### lambdas are useful in functional programming:
```python
>>> Point = namedtuple('Point', field_names=('x',  'y'), defaults=(0,  0))
>>> points = [Point(1, 2), Point(4, 3), Point(2, 4)]
>>> # points sorted by x
>>> sorted(points, key=lambda point: point.x)
[Point(x=1, y=2), Point(x=2, y=4), Point(x=4, y=3)]
>>> # points sorted by x
>>> sorted(points, key=lambda point: point.y)
[Point(x=1, y=2), Point(x=4, y=3), Point(x=2, y=4)]
```


> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY1NzY4ODk1NywtMTM3MTg3OTA3Niw0Mj
k2ODE3MCwtMTc5Nzg1NzI2M119
-->

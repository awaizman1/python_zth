# Iterable
An object that can be passed to [iter()](https://docs.python.org/3/library/functions.html#iter) in order to get an [iterator](https://docs.python.org/3/glossary.html#term-iterator).
```iterator = iter(iterable)```
# Iterator
An object representing a stream of data (finite or infinite).
Calling [next()](https://docs.python.org/3/library/functions.html#next) on an iterator return successive item in the stream. When the stream is exhausted a [StopIteration](https://docs.python.org/3/library/exceptions.html#StopIteration) exception is raised.

> Iterator objects follows the [iterator protocol](https://docs.python.org/3/library/stdtypes.html#typeiter) - required to support ```__next__``` and ```__iter__``` methods.
```python
class SquareIterable:
	def __init__(self, max):
		self._x = 0
		self._max = max

	def __iter__(self):
		return self
	
	def __next__(self):
		ret = self._x**2
		self._x += 1
		
		return 
```
```python
>>> fib_iterable = InfiniteFibTry1()
>>> fib_iterator = iter(InfiniteFibTry1())
>>> print(next(fib_iterator))
1
>>> print(next(fib_iterator))
2
>>> print(next(fib_iterator))
3
>>> print(next(fib_iterator))
5
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNTkzMDc3MTIsLTMxNjMwNDAzNywxMj
Y4Nzg3MTU0LDkyODM1Nzc3NiwxNzI2NTg5MjYyLDMyNjQ0ODYx
MiwtMTk0NzYwMTU1N119
-->
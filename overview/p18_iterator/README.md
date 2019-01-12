# Iterable
An object that can be passed to [iter()](https://docs.python.org/3/library/functions.html#iter) in order to get an [iterator](https://docs.python.org/3/glossary.html#term-iterator).
```python
iterator = iter(iterable)
```

> **Every** python collection is an iterable!

# Iterator
An object representing a stream of data (finite or infinite).
Calling [next()](https://docs.python.org/3/library/functions.html#next) on an iterator return successive item in the stream. When the stream is exhausted a [StopIteration](https://docs.python.org/3/library/exceptions.html#StopIteration) exception is raised.
```python
item = next(iterator)
```

> Iterator objects follows the [iterator protocol](https://docs.python.org/3/library/stdtypes.html#typeiter) - required to support ```__next__``` and ```__iter__``` methods.

## Iterable and iterator as same object (do not!)
```python
class SquareIterable:
	def __init__(self, max):
		self._x = 0
		self.max = max

	def __iter__(self):  # because of this i'm an iterable
		return self
	
	def __next__(self):  # because of this and __iter__ i'm an iterator
		if self._x > self.max:
			raise StopIteration()
		
		ret = self._x**2
		self._x += 1
		
		return ret
```
```python

>>> sqr_iterable = SquareIterable(max=2)
>>> sqr_iterator = iter(sqr_iterable)
>>> print(next(sqr_iterator))
0
>>> print(next(sqr_iterator))
1
>>> print(next(sqr_iterator))
4
>>> print(next(sqr_iterator))
Traceback (most recent call last):
  File ...
  File ..., in __next__
StopIteration
```
```python
>>> for x in SquareIterable(max=2):
...		print(x)
0
1
4
```
> Since both iteratable and iterator are the same object, it can be consumed only once!
```python
>>> sqr_iterable = SquareIterable(max=2)
>>> for x in sqr_iterable:
...		print(x)
0
1
4
>>> for x in sqr_interable:
... 	print(x)
>>>
```
## Separate iterable and iterator objects
```python
class SquareIterable:
	def __init__(self, max):
		self.max = max

	def __iter__(self):  # because of this i'm an iterable
		return SquareIterator(self)

class SquareIterator:
	def __init__(self, sqr_iterable):
		self._sqr_iterable = sqr_iterable
		self._x = 0
	
	def __iter__(self):  # because of this i'm an iterable
		return self
	
	def __next__(self):  # because of this and __iter__ i'm an iterator
		if self._x > self.sqr_iterable.max:
			raise StopIteration()
		
		ret = self._x**2
		self._x += 1
		
		return ret
```
```python

>>> sqr_iterable = SquareIterable(max=2)
>>> for x in sqr_iterable:
...		print(x)
0
1
4
>>> for x in sqr_iterable:
... 	print(x)
0
1
4
```
> Why an iterator must have ```__iter__``` which returns ```self```?
## Time for task:
 - perform ***task.py***
 - test yourself by running ***test_task.py***
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzODA2MzM0MDQsMTY0NjU3MDEwLC02Nj
QyODIwMDgsMTYyNDE4MDQ0MiwtMzE2MzA0MDM3LDEyNjg3ODcx
NTQsOTI4MzU3Nzc2LDE3MjY1ODkyNjIsMzI2NDQ4NjEyLC0xOT
Q3NjAxNTU3XX0=
-->
# Iterable
An object that can be passed to [iter()](https://docs.python.org/3/library/functions.html#iter) in order to get an [iterator](https://docs.python.org/3/glossary.html#term-iterator).
```iterator = iter(iterable)```
# Iterator
An object representing a stream of data (finite or infinite).
Calling [next()](https://docs.python.org/3/library/functions.html#next) on an iterator return successive item in the stream. When the stream is exhausted a [StopIteration](https://docs.python.org/3/library/exceptions.html#StopIteration) exception is raised.

> Iterator objects follows the [iterator protocol](https://docs.python.org/3/library/stdtypes.html#typeiter) - required to support ```__next__``` and ```__iter__``` methods.
```python
class InfiniteFibTry1:
	def __init__():
		self._prev = 1
		self._prev_prev = 0

	def __iter__():
		return self
	
	def __next__():
		curr = self._prev + self._prev_prev
		self._prev_prev = self._prev
		self._prev = curr
		
		return curr
```
```python
>>> for i in InfiniteFibTry1():
...		print(i)

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTI4MzU3Nzc2LDE3MjY1ODkyNjIsMzI2ND
Q4NjEyLC0xOTQ3NjAxNTU3XX0=
-->
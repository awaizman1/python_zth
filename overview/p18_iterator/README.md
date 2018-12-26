# Iterable
An object that can be passed to [iter()](https://docs.python.org/3/library/functions.html#iter) in order to get an [iterator](https://docs.python.org/3/glossary.html#term-iterator).
```iterator = iter(iterable)```
# Iterator
An object representing a stream of data (finite or infinite).
Calling [next()](https://docs.python.org/3/library/functions.html#next) on an iterator return successive item in the stream. When the stream is exhausted a [StopIteration](https://docs.python.org/3/library/exceptions.html#StopIteration) exception is raised.

> Iterator objects follows the [iterator protocol](https://docs.python.org/3/library/stdtypes.html#typeiter) - required to support 

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MTk1MTkwOTcsMzI2NDQ4NjEyLC0xOT
Q3NjAxNTU3XX0=
-->
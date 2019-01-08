# Generator
Generators are functions that can be paused and resumed on the fly, returning an object that can be iterated over.
A generator is lazy evaluated - produces one item at a time and only when asked.

 - Can model infinite sequences (streams)
 - Composable into pipelines
 - Can maintain state and control flow

> Every generator is an iterator.

## Creating a generator
Regular function with ```python
yield``` statement.
```python
def count_to_3():
	yield 1
	yield 2
	yield 3
```

Unlike lists, they are [lazy](https://en.wikipedia.org/wiki/Lazy_evaluation) and thus produce items one at a time and only when asked. So they are much more [memory efficient](https://realpython.com/python-memory-management/) when dealing with large datasets.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEzNzI1OTE1NTgsMTAwMTAzODM2Nl19
-->
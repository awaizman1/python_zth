# Generator
[generator](https://docs.python.org/3/glossary.html#term-generator) is a function that can be paused and resumed on the fly, returning an object that can be iterated over (a [generator iterator](https://docs.python.org/3/glossary.html#term-generator-iterator)).
A generator is lazy evaluated - produces one item at a time and only when asked.

 - Can model infinite sequences (streams)
 - Memory efficient
 - Composable into pipelines
 - Can maintain state and control flow

> Every generator is an iterator.

## Creating a generator
Regular function with ```yield``` statement.
```python
def count_to_2():
    yield 1
    yield 2
```
```python

>>>  g = count_to_2()
>>> next(g)
1
>>> next(g)
2
>>> next(g)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
```python
>>> for i in count_to_2():
... 	print(i)
1
2
```
## Stateful generator
```python
def count():
    num = 0
    while True:
        yield num
        num += 1
```
```python
>>> for i in count():
... 	print(i)
0
1
2
3
4, 5, 6, ...
```
> What need to happen upon yield so that this magic will work?
>
## Pipelines
Generators can be combined into pipelines for natural stream processing.
```python
def even(iterable):
    """
    Generator of even numbers in iterable
    """
    for i in iterable:
        if i % 2 == 0:
            yield i
```
```python
def accumulate(iterable):
    """
    Generator for cumsum of iterable
    """
    total = 0
    for i in iterable:
        total += i
        yield total
```
```python
>>> for i in accumulate(even(count())):
...     print(i)
0
2
6
12
20
30, ...
```
## Generator expression
Similar to list comprehension, one can create generators
```python
g = (x**2 for x in range(1000) if x % 2 == 0)
```
## Builtins iterators and generators
Python introduces many builtin iterators and generators.
Make your self familier with [range](), [zip](https://docs.python.org/3/library/functions.html#zip), [all](https://docs.python.org/3/library/functions.html#all), [any](https://docs.python.org/3/library/functions.html#any), [itertools](https://docs.python.org/3.7/library/itertools.html)
## Time for task:
 - perform ***task.py***
 - test yourself by running ***test_task.py***
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTc2NzU4NjcwNiwtMzUxMjMxODE4LDEwNT
E5NTgxODEsMTYyNzkxOTIzOCwtODM2ODc2NTAwLDE4MjMwNDQ4
NiwxOTg3NzE4MzMsMTAwMTAzODM2Nl19
-->

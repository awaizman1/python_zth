# Generator
Generators are functions that can be paused and resumed on the fly, returning an object that can be iterated over.
A generator is lazy evaluated - produces one item at a time and only when asked.

Unlike lists, they are [lazy](https://en.wikipedia.org/wiki/Lazy_evaluation) and thus produce items one at a time and only when asked. So they are much more [memory efficient](https://realpython.com/python-memory-management/) when dealing with large datasets.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTU3NTg4MjEyNF19
-->
# Classes
```python
class Dog:                                     # class definition
    instances_count = 0                        # class member (shared by all instances)

    def __init__(self, name, age):             # instance initialization method (not a constructor)

        self.name = name                       # instance member
        self.age = age                         # instance member
        Dog.instances_count += 1               # modifying class member
    
    def bark(self):                            # instance method
        print(f"{self.name} is barking...")
```
```python
>>> # instantiating a class
>>> bolt = Dog(name='bolt', age=3)
>>> # access instance members
>>> bolt.name
"bolt"
```
## Public / Protected / Private
“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python.
[private variables](https://docs.python.org/3/tutorial/classes.html#private-variables)
There is a convention in python (which is already enforced by IDEs, linters, etc.) - a named prefixed with underscore should be treated as private.

> There is also a way to get name-mangling (i.e. ```__spam```) - usually not needed, avoid it.

```python
class RedisClient:

    def __init__(self, host, port):
    
        self.host = host                                # public member
        self.port = port                                # public member
        self._connection = self._connect(host, port)    # private member
    
    def _connect(host, port):                           # private instance method
        ...
    
    def set(self, key, data):                           # public instance method
        ...
    
    def get(self, key):                                 # public instance method
        ...
```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMDQzODEyNzMsLTEzOTM3MzE5MSwtNz
Q5OTUxNTEzLC0xNTY2MjE4ODUzLDcxNjQ0MzE3M119
-->
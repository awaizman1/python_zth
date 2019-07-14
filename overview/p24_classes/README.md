# Classes
```python
class Dog:                                     # class definition
    instance_count = 0                        # class member (shared by all instances)

    def __init__(self, name, age):             # instance initialization method (not a constructor)

        self.name = name                       # instance member
        self.age = age                         # instance member
        Dog.instance_count += 1               # modifying class member
    
    def bark(self):                            # instance method
        print(f"{self.name} is barking...")
```
```python
>>> # instantiating a class
>>> bolt = Dog(name='bolt', age=3)
>>> # access instance members
>>> bolt.name
'bolt'
>>> # access class members (via class or instance)
>>> Dog.instance_count
1
>>> bolt.instance_count
1
>>> # access instance methods (note 'self' is implicit bounded)
>>> bolt.bark()
'bolt is barking...'
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
## Static methods and class methods
### static method
It is preferred to define a method which doesn't depend on instance's state (```self```) as static one.
[staticmethod](https://docs.python.org/3/library/functions.html#staticmethod)

> **Unlike other languages, in python static methods can be overridden in sub-classes**

```python
class Dog:

    def __init__(self, name=None, age=0):

        self.name = self._get_random_name() if name else name
        self.age = age
    
    @staticmethod
    def _get_random_name():                   # a static method (notice 'self' is missing)
        ...
```
### class method
Another form of static method in python is a [class method]( https://docs.python.org/3/library/functions.html#classmethod). Similar to static method, but receives the class as implicit first argument.
```python
class Dog:

    def __init__(self, name=None, age=0):

        self.name = self._get_random_name() if name else name
        self.age = age
    
    @classmethod
    def create_newborn(cls, name):                   # a class method (notice 'cls' argument)
        return cls(name, age=0)
```
## Properties
Consider our Dog.
```python
>>> bolt = Dog(name='bolt', age=3)
>>> bolt.name = 'puppy'  # probably a violation of what Dog writer meant...
```
## Try #1 - private member with getter / setter
```python
class Dog:
    instance_count = 0

    def __init__(self, name, age):

        self._name = name                     # now name is private
        self._age = age                       # now age is private
        Dog.instance_count += 1
    
    def bark(self):                           # instance method
        print(f"{self.name} is barking...")
    
    def get_name(self):                       # getter for name
        return name
    
    def get_age(self):                        # getter for age
        return age
```
***Issues:***

 - non pythonic - access attributes directly and not via setter/getter
 - boilerplate code of setter/getter
 - all consumer must modify their code to use ```get_name```
## Try #2 - properties
[property](https://docs.python.org/3/library/functions.html#property) is a superior python alternative for getter/setter.
Can be used for getter, setter and deleter as required.
```python
class Dog:
    instance_count = 0

    def __init__(self, name, age):

        self._name = name                     # now name is private
        self._age = age                       # now age is private
        Dog.instance_count += 1
    
    def bark(self):                           # instance method
        print(f"{self.name} is barking...")
    
    @property
    def name(self):                       # getter for name
        return name
    
    @property
    def age(self):                        # getter for age
        return age
```
```python
>>> bolt = Dog(name='bolt', age=3)
>>> bolt.name  # accessing property as regular attribute
'bolt'
>>> bolt.name = 'puppy'  # probably a violation of what Dog writer meant...
```
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYyMDI4NjI2MiwxOTU0NDQ3NCwyMDkyNj
E5NTMxLDE5MTg1Njc4OTYsMTgxMDA4NDQzMCwtMzA3MTU2NDcw
LDMzMDYxNTYyOSwtMTM5MzczMTkxLC03NDk5NTE1MTMsLTE1Nj
YyMTg4NTMsNzE2NDQzMTczXX0=
-->
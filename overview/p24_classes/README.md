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
## Public / Protected / Private
“Private” instance variables that cannot be accessed except from inside an object don’t exist in Python.
[private variables](https://docs.python.org/3/tutorial/classes.html#private-variables)
There is a convention in python (which is already enforced by IDEs, linters, etc.) - a named prefixed with underscore should be treated as private.
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM1MzY0MDE0OCwtNzQ5OTUxNTEzLC0xNT
Y2MjE4ODUzLDcxNjQ0MzE3M119
-->
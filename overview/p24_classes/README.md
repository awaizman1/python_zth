# Classes
```python
class Dog:                                     # class definition
    instances_count = 0

    def __init__(self, name, age):

        self.name = name
        self.age = age
        Dog.instances_count += 1
    
    def bark(self):
        print(f"{self.name} is barking...")
```

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg2NjM0NTkwLDcxNjQ0MzE3M119
-->
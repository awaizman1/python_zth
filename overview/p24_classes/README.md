# Classes
```python
class Dog:                                     # class definition
    instances_count = 0                        # class member (shared by all instances)

    def __init__(self, name, age):

        self.name = name                       # instance member
        self.age = age                         # instance member
        Dog.instances_count += 1               # modifying class member
    
    def bark(self):
        print(f"{self.name} is barking...")
```

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzc2MzE2NzU2LDcxNjQ0MzE3M119
-->
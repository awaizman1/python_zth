# Classes
```python
class Dog:                                     # class definition
    instances_count = 0                        # class member (shared by all instances)

    def __init__(self, name, age):

        self.name = name                       # instance member
        self.age = age                         # instance member
        Dog.instances_count += 1               # modifying class member
    
    def bark(self):                            # member function
        print(f"{self.name} is barking...")
```

> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk2OTI5NTU5OSw3MTY0NDMxNzNdfQ==
-->
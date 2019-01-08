# Exceptions
```python
try:
	a_num = int(a)
	b_num = int(b)
	c = a_num / b_num
	
except ZeroDivisionError:  # except single exception
	print("can't divide by 0")
except (ValueError, TypeError):  # except multiple exceptions
	print("did you call 'int(..)' with a str? does it represent a number?")
except 
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkzODgyNjI5NiwtMTY3NTQyMjczNV19
-->
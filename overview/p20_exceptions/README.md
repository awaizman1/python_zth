# Exceptions
```python
try:
	a_num = int(a)
	b_num = int(b)
	return a_num / b_num
except ZeroDivisionError:
	print("can't divide by 0")
except (ValueError, TypeError):
	print("did you call 'int(..)' with a str? does it represent a number?")
except 
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NzU0MjI3MzVdfQ==
-->
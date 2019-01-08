# Exceptions
```python
try:
	a_num = int(a)
	b_num = int(b)
	c = a_num / b_num
	with open(r"C:\out.txt", "wt") as f:
		f.write(str(c))
except ZeroDivisionError:  # except single exception
	print("can't divide by 0")
except (ValueError, TypeError):  # except multiple exceptions
	print("did you call 'int(..)' with a str? does it represent a number?")
except OSError as e:  # access the exception instance
	print(e)
```
```python
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDg0NDM4MzU2LDE5Mzg4MjYyOTYsLTE2Nz
U0MjI3MzVdfQ==
-->
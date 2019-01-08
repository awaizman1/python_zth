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
except OSError as e:
	print(e)
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2MDMwMjI1ODYsMTkzODgyNjI5NiwtMT
Y3NTQyMjczNV19
-->
# if, else, elif
```python
if x > 10:
	print(">10")
else:
	print("<=10")
```
```python
if x > 10:
	print(">10")
else:
	if x < 0:
		print("<0")
	else:
		print("0<=x<=10")
```

> Zen: ***flat is better than nested.***

```python
if x > 10:
	print(">10")
elif x < 0:
	print("<0")
else:
	print("0<=x<=10")
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTY5MzgxMzExXX0=
-->
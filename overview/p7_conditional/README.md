# if, else, elif
```python
if x > 10:
	print(">10")
else:
	print("<=10")
```
## Remember the zen
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
## Conditional expression
The expression `x  if  C  else  y` first evaluates the condition, _C_ rather than _x_. If _C_ is true, _x_ is evaluated and its value is returned; otherwise, _y_ is evaluated and its value is returned.
```python
a = 5 if x > 0 else -5
print("y") if x else print("n")
```
### Time for task:
 - perform ***task.py***
 - test yourself by running ***test_task.py***
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NDcyODk3MjgsOTY5MzgxMzExXX0=
-->
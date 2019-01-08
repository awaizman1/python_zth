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
## else clause
Useful for code that must be executed if the try clause **does not** raise an exception.
```python
try:
	f = open('file.txt', 'r')
    except OSError:
        print('cannot open')
    else:
        print('file has', len(f.readlines()), 'lines')
        f.close()
```
What is the difference from:
```python
try:
	f = open('file.txt', 'r')
	print('file has', len(f.readlines()), 'lines')
    f.close()

    except OSError:
        print('cannot open')
    else:
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzg5ODE3NjM4LDE5Mzg4MjYyOTYsLTE2Nz
U0MjI3MzVdfQ==
-->
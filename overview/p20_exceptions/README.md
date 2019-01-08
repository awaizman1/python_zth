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
## Raise an exception
```python
if something_went_wrong:
	raise RuntimeError("bad")
```
## finally clause
Always prefer ```context managers``` over ```finally``` for cleanups!
```python
try:
	raise RuntimeError
finally:
	print("nothing can bypass me")
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

> Q: why not put else clause code in try block?

```python
try:
	f = open('file.txt', 'r')
	print('file has', len(f.readlines()), 'lines')
    f.close()
except OSError:
    print('cannot open')
```

> A: avoids accidentally catching an exception that wasn’t raised by the code being protected by the `try` … `except` statement.
## User-defined exceptions
Think twice before creating new exception type!
That was the first time, now think again...!
> Usually [built-in exceptions](https://docs.python.org/3/library/exceptions.html#exception-hierarchy) are sufficient.

If you are still sure:
- Derive from [Exception](https://docs.python.org/3/library/exceptions.html#Exception) class (directly or indirectly)
- Name it XXX
```python
class MyFancyError(Exception):
	pass
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkxMTA1NTU2LC05NzI5NDgwMzAsLTY3Mz
IyMjc1MSwxOTM4ODI2Mjk2LC0xNjc1NDIyNzM1XX0=
-->
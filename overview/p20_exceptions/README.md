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
    raise RuntimeError("bad")  # bare raise
```
```python
try:
    raise RuntimeError("bad")
except RuntimeError:
    do_something()
    raise  # re-raise
```

> When raising an exception, pass a single str argument which describes the error.
> Don't exploit the fact that exception can take arbitrary args, it's only for backwards ([pep-352](https://www.python.org/dev/peps/pep-0352/#id6)).

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
- Name it XXX**Error** (and not XXXException)
```python
class MyFancyError(Exception):
    pass

class MyOtherFancyError(MyFancyError):
    def __init__(special_info):
        this.special_info = special_info
```
## Exception chaining - ```__cause__``` and ```__context__``` attributes
Chaining exceptions is done implicitly and can be done explicitly.
[raise-statement](https://docs.python.org/3/reference/simple_stmts.html#the-raise-statement)
### Implicitly
```python
try:
    raise ValueError
except Exception as e:
    raise IndexError
```
```python
Traceback (most recent call last):
  File "tmp.py", line 2, in <module>
    raise ValueError
ValueError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "tmp.py", line 4, in <module>
    raise IndexError
IndexError
```

> ```raise``` in an exception handler sets the ```__context__``` attribute

### Explicitly
```python
try:
    raise ValueError
except Exception as e:
    raise IndexError from e
```
```python
Traceback (most recent call last):
  File "tmp.py", line 2, in <module>
    raise ValueError
ValueError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "tmp.py", line 4, in <module>
    raise IndexError from e
IndexError
```

> ```raise from``` sets the ```__cause__``` attribute
> 
> ```raise from None``` will suppress the ```__context__``` - useful in case you don't want the don't want the "_during handling another exception happened_" message
## Tips
- Built-in exceptions are often the best choice.
- Avoid protecting against TypeError (it is un-pythonic, cumbersome the code) - rely on type checking.
## Traceback
Every ```Exception``` has a ```__traceback__``` attribute - holding its associated [traceback object](https://docs.python.org/3.7/library/traceback.html).
> A traceback object holds all stack frames and its local variables. Don't reference traceback objects for long, otherwise all those frames and variables won't be freed!

```python
import traceback

try:
    raise ValueError("blabla")
except ValueError as e:
    print("------->traceback is an object")
    print(e.__traceback__)
    print("------->print a traceback object")
    traceback.print_tb(e.__traceback__)
    print("------->print current handled exception with traceback")
    traceback.print_exc()
```
```python
------->traceback is an object
<traceback object at 0x1038c3e88>
------->print a traceback object
File "<stdin>", line 2, in <module>
------->print current handled exception with traceback
Traceback (most recent call last):
File "<stdin>", line 2, in <module>
ValueError: blabla
```
## Assertion
The [assert](https://docs.python.org/3.7/reference/simple_stmts.html?highlight=assert#the-assert-statement) statement is used to insert debugging assertions into a program .
```python
assert expression1 [,expression2]
```
is equivalent to:
```python
if __debug__:
    if not expression1: raise AssertionError(expression2)
```

> ```__debug__``` is by default True. You can set it to False by running the interpreter with [-O](https://docs.python.org/3.7/using/cmdline.html#cmdoption-o) option.

```python
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def print_color(color):
    if color == Color.RED:
        print("red")
    elif color == Color.GREEN:
        print("green")
    elif color == Color.BLUE:
        print("blue")
    else:
        assert False, "unknown color"
```

## EAFP
It's **E**asier to **A**sk **F**orgiveness than **P**ermission.
### Ask for permission approach
```python
def handle_file(filename):
    if not os.path.exists(filename):
        print("missing file")
        return
		
    if not has_read_access(filename):
        print("no read access to file")
	
    # more validations...

    # do the actual work
    process_file(filename)
```
- hurts readability
- practically impossible to validate all (what about race conditions here?, what is the the file is garbage?)
### EAFP approach

> Python preferred way

```python
def handle_file(filename):
	
    try:
        # do the actual work
        process_file(filename)
    except OSError as e:
        print("failed to handle file because: ", e)
```
## Time for task:
perform ***task.py*** and ***task2.py***
test yourself by running ***test_task.py*** and ***test_task2.py***
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTkxMTAwNTYyMCwtMTgxNzIyODA2NSwtMT
U0NjU5MDk4OCwtODkzNTY0ODcxLC0xNzg4ODgxMzI4LDEwODY3
MzU4NjIsMTQzNjE0MDE0OSwtMjg2MzAzMDI2LDY1OTkyNzMyMy
wtOTcyOTQ4MDMwLC02NzMyMjI3NTEsMTkzODgyNjI5NiwtMTY3
NTQyMjczNV19
-->

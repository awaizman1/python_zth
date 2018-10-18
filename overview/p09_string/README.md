# str
***Immutable*** sequence of unicode codepoints
- immutable - means you can't modify str content
- sequence - follows the sequence protocol
## str literals
```python
'this is a literal string'
"this is a literal string too"

# literal str concatenation (don't use '+' for literal str concatenation)
>>> s = "hello" " world"
>>> s
'hello world'

>>> print("this is a very long line so i split it to two: "
>>> 	"first part and "
>>> 	"second part")
'this is a very long line so i split it to two: first part and second part'

# multiline str
"this is a\n multiline str"

"""this is a
multiline str too"""

'''this is a
multiline str too'''
```

> ***'\n'*** is a universal newline in python - io in text mode will automatically translate ***'\n'*** to/from native newline
> https://pythonconquerstheuniverse.wordpress.com/2011/05/08/newline-conversion-in-python-3/
```python
# escape char in literals
"say \"hello\""
'say "hello" better'

# raw str
"instead of C:\\foo\\goo"
r"C:\foo\goo"
```
```python
# format strings (f-string)
>>> today = datetime.now()
>>> f"today is {today} tomorrow is {today + datetime.timedelta(days=1)}"
'today is 2018-10-18 14:38:53.204763 tomorrow is 2018-10-19 14:38:53.204763'

# raw f-string
>>> rf"C:\tmp\{'general' if user is None else 'user'}"
'C:\\tmp\\user'
```
## Convert objects to str
Use the ***str*** constructor
```python
>>> str(5)
'5'
>>> str(datetime.now())
'2018-10-04 21:24:43.201961'
```

## str as sequence protocol
```python

>>> s = "hello world"
>>> len(s)
11
>>> s + s
"hello worldhello world"
>>> s * 3
"hello worldhello worldhello world"
>>> s[1]
'e'
>>> s[1:5]
'ello'
>>> s.count('o')
2
>>> 'o' in s
True
>>> 'hell' in s
True
>>> 'z' in s
False
>>> o.index('e')
1
>>> s.index('world')
6
>>> list(s)
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> tuple(s)
('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
>>> s += " again"
>>> s
'hello world again'
>>> s *= 2
>>> s
'hello world againhello world again'
```
### All of the below statement gives TypeError (although part of sequence protocol) - why?
```python
>>> s[4]
>>> del s[4]
>>> s[1:3] = 'abc'
>>> del s[1:3]
```
## *str* format
### `printf`-style
[printf-style-string-formatting](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)
```python
>>> name = "Bob"
>>> grade = 93

# positional substitution
>>> "The grade of %s is %d in hex 0x%x" % (name, grade, grade)
'The grade of Bob is 93 in hex 0x5d'
```
```python
# named substitution
>>> "The grade of %(student_name)s is %(grade)d in hex 0x%(grade)x" % {"grade": grade, "student_name": name}
'The grade of Bob is 93 in hex 0x5d'
```
### Format string style
[format-string-syntax](https://docs.python.org/3/library/string.html#format-string-syntax)
```python
# positional substitution
>>> "The grade of {} is {} in hex 0x{:x}".format(name, grade, grade)
'The grade of Bob is 93 in hex 0x5d'

>>> "The grade of {1} is {0} in hex 0x{0:x}".format(grade, name)
'The grade of Bob is 93 in hex 0x5d'
```
```python
# named substitution
>>> "The grade of {student_name} is {grade} in hex 0x{grade:x}".format(student_name=name, grade=grade)
'The grade of Bob is 93 in hex 0x5d'
```
```python
# named attribute and index lookup
>>> class Student:
>>> ...	def __init__(name, grade):
>>> ... 	self.name = name
>>> ...		self.grade = grade
>>>
>>> bob = Student("Bob", 93)
>>>
>>>"The grade of {student.name} is {student.grade}".format(student=bob)
'The grade of Bob is 93'

>>>"The grade of {student[0]} is {student[1]}".format(student=("Bob", 93))
'The grade of Bob is 93'
```
### f-string
As you already saw above, all you need to know is that f-string uses the same ***format()*** protocol as in (# Format-string-style)
> 
> 
> **Advanced:** you can implement your own formatting specifiers and control how your objects will be formatted by overriding ***\_\_format\_\_***

    

### Time for task:
 - perform ***task.py*** and ***task2.py***
 - test yourself by running ***test_task.py*** and ***test_task2.py***
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzkzODg2MDE3LC0xMTI4ODgyOTgxLDE3ND
k3OTM3NzksLTkwMTM0MzQwOCwxMDgyNTU3NTc1LC0xODg1MzAz
MTMzLC02ODc1MDIzMzMsLTE4NDc2MTQyMDksLTEwNTQwNDc3OT
AsODIzMTYyNjM4LDgyMTg1NTUxOCwtMzE2MTI3NDY1LC0xMzY3
Nzk2MDA3LDE4MDM2MDM5NDhdfQ==
-->
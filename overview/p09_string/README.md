# str
Immutable sequence of unicode codepoints
- immutable - means you can't modify str content
- sequence - follows the sequence protocol
## str literals
```python
'this is a literal string'
"this is a literal string too"

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
today = datatime.now()
f"today is {today} tomorrow is {today + datetime.timedelta(days=1)}"

# raw f-string
rf"C:\tmp\{'general' if user is None else 'user'}"
```
## str as sequence
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
>>> s[4]
>>> del s[4]
>>> s[1:3] = 'abc'
>>> del s[1:3]

```
### Time for task:
 - perform ***task.py*** and ***task2.py***
 - test yourself by running ***test_task.py*** and ***test_task2.py***
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzEyNjI3NDk2LDgyMzE2MjYzOCw4MjE4NT
U1MTgsLTMxNjEyNzQ2NSwtMTM2Nzc5NjAwNywxODAzNjAzOTQ4
XX0=
-->
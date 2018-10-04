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
f"
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExNzkzNjU1MjQsLTMxNjEyNzQ2NSwtMT
M2Nzc5NjAwNywxODAzNjAzOTQ4XX0=
-->

# bytes
Immutable sequence of bytes
- immutable - means you can't modify str content
- sequence - follows the sequence protocol
https://docs.python.org/3/library/stdtypes.html#bytes-objects

> All sequence common operations can be applied to bytes too (similar to str)

## bytes literals
```python
b'this is a bytes literal'
b"this is a bytes literal too"

#with hex values
b"\xCA\xFE"
```
## Converting to / from str
Convert bytes to / from str using ***encode / decode*** methods.
[encode](https://docs.python.org/3/library/stdtypes.html#str.encode)
[decode](https://docs.python.org/3/library/stdtypes.html#str.encode)
# bytearray
Mutable counterpart of bytes
https://docs.python.org/3/library/stdtypes.html#bytearray-objects
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMTM4MzcxMTYsODU2Mjc0MjIwLC05Mz
YxMjUxMjgsMTM5NDQ4NTA4MCwyNjcyOTk5MDUsLTIwOTE1OTk5
OV19
-->
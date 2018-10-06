
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
[decode](https://docs.python.org/3/library/stdtypes.html#bytes.decode)
# bytearray
Mutable counterpart of bytes
https://docs.python.org/3/library/stdtypes.html#bytearray-objects
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzg3MzQ4MjU4LDg1NjI3NDIyMCwtOTM2MT
I1MTI4LDEzOTQ0ODUwODAsMjY3Mjk5OTA1LC0yMDkxNTk5OTld
fQ==
-->
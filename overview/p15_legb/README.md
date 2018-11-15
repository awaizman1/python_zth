# Variable Scoping Rules
Whenever the interpreter accesses a variable (named reference), it follows the scoping rules:

 1. **Local** - inside the current function.
 2. **Enclosing** - any enclosing function.
 3. **Global** - module top level
 4. **Built-in** - provided by the `builtins` module

> if, for, while, with blocks doesn't add new scope

```python
count = 0

def print_count():
    print(count)

def set_count(value):
    count = value
``` 
```python
import 
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAyODAxMDMwMV19
-->
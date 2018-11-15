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

def inc_count():
    count = count + 1
``` 

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTgyMzE0MTAzOV19
-->
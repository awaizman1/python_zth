# Function
The smallest granularity of reusable code
```python
# syntax
def functionname( args ):
    "function_docstring"
    function_suite
    return [expression]
```
```python
# example
def foo(x, y, z):
    return x + y + z
```
# Module
A collection of functions and source code in a single ***.py*** file.  
[modules](https://docs.python.org/3/tutorial/modules.html#modules)  
 ### fibo.py
![](/images/p14-1.png)
## Reusing a module
A module can be either imported by another module or run directly by the interactive interpreter.
```python
# greet.py module

def print_greeting():
    print('have a nice day')

print_greeting()
```
#### Importing a module
```python
# my_module.py module

import greet

greet.print_greeting()
```

> Executing ***my_moudle.py*** will print 'have a nice day' twice. **Why?**

#### Running a module from interactive interpreter
```cmd
$ python greet.py
have a nice day
```
#### Distinguish between import and running as a script
module's [\_\_name\_\_ ](https://docs.python.org/3/library/__main__.html) global variable is set to "\_\_main\_\_" if running as script, otherwise it is the module name.
```python
# greet.py module - fixed!

def print_greeting():
    print('have a nice day')

if __name__=="__main__":
    print_greeting()
```
## Recommanded scriptable module layout

 - add main() function which runs script logic
 - if \_\_name\_\_ == \_\_main\_\_ should call main()
Intoducing the 

```python
# main.py module

def some_func(args):
    ...

def parse_args():
    ...

def main():
    args = parse_args()
    some_func(args)

if __name__ == "__main__":
    main()
```
# Package
A collection of modules (sub-modules) and other packages (sub-packages).
![](/images/p14-2.png)
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQwODA3MTc1OCwxMDk2NTUxNjU5LDY1Nj
Y4Mzc3LC0yMDMzMzE3MTQ0LDE0NDQ0Nzc1NjcsMTAxMjk4MzU5
Nl19
-->
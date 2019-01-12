# Virtual environment
Virtual environment is a light-weight, isolated python environment.  
Every virtual environment can hold its own dependencies with specific versions.  

![](/images/p21-venv.PNG)
## Working with virtual envs
### Create virtual env
```cmd
$ python -m venv my_venv
```
### Activate virtual env
```cmd
$ my_venv\Scripts\activate
```
Notice how prompt changes after activation:
```cmd
(my_venv) $
```
Now you can install packages into environment:
```cmd
(my_venv) $
### Deactivate virtual env
```cmd
(my_venv) $ deactivate
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTY0MzUzNjk3OSw3NzkwNzkyMTYsMjExMD
UxMTU0NywtNzYwOTY4MDg3LDE0NTM1Nzg2MzQsLTExMDI0NDg5
NzUsMTk0MjA0MDk0OV19
-->
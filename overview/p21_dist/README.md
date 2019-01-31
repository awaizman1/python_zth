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
(my_venv) $ python -m pip install numpy==1.0
```
### Deactivate virtual env
```cmd
(my_venv) $ deactivate
```
## Time for task:
 - create 2 new virtual envs: ```env1``` & ```env2```.
 - install the latest ```numpy``` into ```env1``` and ```numpy 1.14``` into ```env2```.
 - validate that each env refers to the correct numpy version.
# PIP - PIP Installs Packages
[PyPA](https://www.pypa.io/en/latest/) recommended tool for installing python packages.
Usually, packages are stored in [PyPI](https://pypi.org/) repo but can also reside in private repos, file system, etc.

```python
(my_venv) $ python -m pip install numpy
```

```python
(my_venv) $ python -m pip install numpy==1.14
```

```python
(my_venv) $ python -m pip install numpy
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI3MzQwNTc0MSwtMTk5MzA1NzM5NiwtNT
M1MTY2NDYsMTE0MzU4Mzg0OSw3NzkwNzkyMTYsMjExMDUxMTU0
NywtNzYwOTY4MDg3LDE0NTM1Nzg2MzQsLTExMDI0NDg5NzUsMT
k0MjA0MDk0OV19
-->
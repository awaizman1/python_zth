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
### Install latest
```bash
(my_venv) $ python -m pip install numpy
```
### Install specific version
```bash
(my_venv) $ python -m pip install numpy==1.14
```
### Install from wheel
```bash
(my_venv) $ python -m pip install numpy==1.14
```
### Uninstall package
```bash
(my_venv) $ python -m pip uninstall numpy
```
### Search for a package
```bash
(my_venv) $ python -m pip search numpy
```
### List installed packages
```bash
(my_venv) $ python -m pip list
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MDYzMTgwNzcsLTU5NDIzMjIwNywtMT
k5MzA1NzM5NiwtNTM1MTY2NDYsMTE0MzU4Mzg0OSw3NzkwNzky
MTYsMjExMDUxMTU0NywtNzYwOTY4MDg3LDE0NTM1Nzg2MzQsLT
ExMDI0NDg5NzUsMTk0MjA0MDk0OV19
-->
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
PyP
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY4Nzg3ODE5LDExNDM1ODM4NDksNzc5MD
c5MjE2LDIxMTA1MTE1NDcsLTc2MDk2ODA4NywxNDUzNTc4NjM0
LC0xMTAyNDQ4OTc1LDE5NDIwNDA5NDldfQ==
-->
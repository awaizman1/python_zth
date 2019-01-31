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
# PIP - *P*IP *I*nstalls *P*ackages
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
(my_venv) $ python -m pip install numpy-1.16.0-cp36-cp36m-win_amd64.whl
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
### Freeze environment
```bash
(my_venv) $ python -m pip freeze > requirements.txt
```
### Install from requirements file
```bash
(my_venv) $ python -m pip install -r requirements.txt
```
## Time for task:
 - using virtual env ```env2``` from above:
	 - upgrade numpy to latest
	 - list all installed packages
	 - create new virtual env ```venv3``` which is identical to ```venv2``` (using requirements file)
# Distributing your own package
## Recommended project layout
```
my_project
	package_a
		__init__.py
		some_module.py
	tests
		__init__.py
		test_some_module.py
	
	setup.py
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzg0ODA5MTczLC0xMjQyMjkxNTE3LC01OT
QyMzIyMDcsLTE5OTMwNTczOTYsLTUzNTE2NjQ2LDExNDM1ODM4
NDksNzc5MDc5MjE2LDIxMTA1MTE1NDcsLTc2MDk2ODA4NywxND
UzNTc4NjM0LC0xMTAyNDQ4OTc1LDE5NDIwNDA5NDldfQ==
-->
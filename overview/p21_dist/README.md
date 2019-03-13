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
(my_venv) $ python -m pip install numpy==1.14
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
[packaging python projects](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects)
## Recommended project layout
```
/my_project						project root
	/fancy_tool					project package
		__init__.py
		some_module.py
	/tests						project package tests
		__init__.py
		test_some_module.py
	
	setup.py					build script for setuptools
```
## setup.py bare minimum
```python
from setuptools import setup

setup(
    name="fancy-tool",
    version="0.0.1",
    # author="Example Author",
    # author_email="author@example.com",
    # description="A small example package",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(exclude=["tests*"]),
    install_requires=[
        numpy==1.14
    ]
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    #     "License :: OSI Approved :: MIT License",
    #     "Operating System :: OS Independent",
    # ],
)
```
## Generating your distribution archive
```bash
$ python setup.py bdist_wheel
```
Now you will get your distribution wheel:
```bash
/dist
	fancy_tool-0.0.1-py3-none-any.whl
```
This distribution can be uploaded to PyPI / other repo or could be shared with others.
## Time for task:
You wrote a nice package ```cpu_utilization``` which you would like to share with others.
the package can monitor system cpu utilization and alert if it reaches some threshold.

 - get familiar with ```cpu_utilization``` - what external packages dependencies does it use?
 - create a venv, install dependencies into it and run the ```cpu_utilization``` test in it.
 - add setup.py to your project in order to make it distributable.
 - now, dist your package as a wheel.
 - inside a fresh venv (not the previous one), install the ```cpu_utilization``` dist and test that it works.

> **Make sure you didn't have to install ```cpu_utilization``` dependencies manually in order to make it run!!!**

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTUwODY5OTkxOSw4Njc3MTQwNjMsMTgyOT
UxOTc0MywtMTQyMTYzMjQyNywtNTUwMjMwMjMzLC0xMjQyMjkx
NTE3LC01OTQyMzIyMDcsLTE5OTMwNTczOTYsLTUzNTE2NjQ2LD
ExNDM1ODM4NDksNzc5MDc5MjE2LDIxMTA1MTE1NDcsLTc2MDk2
ODA4NywxNDUzNTc4NjM0LC0xMTAyNDQ4OTc1LDE5NDIwNDA5ND
ldfQ==
-->

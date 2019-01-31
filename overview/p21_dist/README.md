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
[packaging python projects](https://packaging.python.org/tutorials/packaging-projects/#packaging-python-projects)
## Recommended project layout
```
/my_project
	/fancy_tool
		__init__.py
		some_module.py
	/tests
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
    packages=setuptools.find_packages(),
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
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MjE2MzI0MjcsLTU1MDIzMDIzMywtMT
I0MjI5MTUxNywtNTk0MjMyMjA3LC0xOTkzMDU3Mzk2LC01MzUx
NjY0NiwxMTQzNTgzODQ5LDc3OTA3OTIxNiwyMTEwNTExNTQ3LC
03NjA5NjgwODcsMTQ1MzU3ODYzNCwtMTEwMjQ0ODk3NSwxOTQy
MDQwOTQ5XX0=
-->
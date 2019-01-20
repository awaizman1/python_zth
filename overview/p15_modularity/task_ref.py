import sys

# adding dir_not_in_path to sys.path - ALTERING sys.path IS USUALLY A BAD PRACTICE, THIS IS ONLY FOR LEARNING PURPOSE
sys.path.append("dir_not_in_path")

import some_module


some_module.foo()

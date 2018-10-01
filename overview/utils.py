import inspect
import sys
from subprocess import run

def get_task_module_name():

    for frame in inspect.stack():
        if frame.filename.endswith('test_task.py'):
            test_task_module_name = inspect.getmodule(frame.frame).__name__
            return test_task_module_name.replace("test_task", "task")


def run_test_and_get_output():
    task_module_name = get_task_module_name()
    print(f"Running: {sys.executable} -m {task_module_name}")
    ret = run([sys.executable, '-m', task_module_name], capture_output=True, text=True)
    return ret.stdout


def check_output(expected_output):
    output = run_test_and_get_output()

    if expected_output != output:
        raise AssertionError(f"""expected_output != output
expected_output:
{expected_output}

ouput:
{output}""")

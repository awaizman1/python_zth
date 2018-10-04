import inspect
import sys
from subprocess import run, PIPE, STDOUT

def get_task_module_name(run_task_ref):

    for frame in inspect.stack():
        if frame.filename.endswith('test_task.py'):
            test_task_module_name = inspect.getmodule(frame.frame).__name__
            task_module_name = "task_ref" if run_task_ref else "task"
            return test_task_module_name.replace("test_task", task_module_name)


def run_test_and_get_output(run_task_ref):
    task_module_name = get_task_module_name(run_task_ref)
    print(f"Running: {sys.executable} -m {task_module_name}")
    ret = run([sys.executable, '-m', task_module_name], stdout=PIPE, stderr=STDOUT, universal_newlines=True)
    return ret.stdout


def check_output(expected_output, run_task_ref = False):
    output = run_test_and_get_output(run_task_ref)

    if expected_output != output:
        raise AssertionError(f"""expected_output != output
expected_output:-->
{expected_output}<--

ouput:-->
{output}<--""")

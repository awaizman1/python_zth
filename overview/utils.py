import inspect
import re
import sys
from subprocess import run, PIPE, STDOUT


def get_task_module_name(run_task_ref):
    for frame in inspect.stack():
        match = re.search(r"(test_task(\d*))\.py", frame.filename)
        if match:
            test_task_module_name = inspect.getmodule(frame.frame).__name__
            task_module_name = f"task{match[2]}_ref" if run_task_ref else f"task{match[2]}"
            return test_task_module_name.replace(match[1], task_module_name)

    raise RuntimeError("Can't find task module")


def run_test_and_get_output(input, run_task_ref=False):
    task_module_name = get_task_module_name(run_task_ref)
    print(f"Running: {sys.executable} -m {task_module_name}")
    ret = run([sys.executable, '-m', task_module_name], input=input, stdout=PIPE, stderr=STDOUT,
              universal_newlines=True)
    return ret.stdout


def check_output(expected_output, input=None, run_task_ref=False):
    output = run_test_and_get_output(input, run_task_ref)

    if expected_output != output:
        raise AssertionError(f"""expected_output != output
expected_output:-->
{expected_output}<--

ouput:-->
{output}<--""")


def check_samples(samples, run_task_ref=False):
    for input_, expected_output in samples:
        check_output(expected_output, input_, run_task_ref)

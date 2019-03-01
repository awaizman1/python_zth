# write a function 'async_run' which is capable of running any function async on a  dedicated thread
# for example:
# having a function foo(a, b), one can run it async using 'async_run':
# async_run(foo, a, b)
# async_run(foo, a=1, b=2)
# async_run(foo, 1, b=2)
import threading
import time


def async_run(func, *args, **kwargs):
    threading.Thread(target=func, args=args, kwargs=kwargs).start()


def foo(a, b):
    print(f"running foo on ({a}, {b}) in thread {threading.get_ident()}")
    time.sleep(1)


async_run(foo, 1, 2)
async_run(foo, b=2, a=1)
async_run(foo, 1, b=2)

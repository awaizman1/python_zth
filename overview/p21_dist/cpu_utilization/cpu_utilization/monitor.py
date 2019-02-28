import threading
import time

import psutil


def start(max_utilization):

    threading.Timer(1, _check_utilization, args=(max_utilization,)).start()


def _check_utilization(max_utilization):

    utilization = psutil.cpu_percent()
    if utilization > max_utilization:
        print("cpu utilization is high: ", utilization)

    timer = threading.Timer(1, _check_utilization, args=(max_utilization,))
    timer.daemon = True
    timer.start()


if __name__ == "__main__":
    start(0)

    while True:
        time.sleep(10)

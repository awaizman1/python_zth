from unittest import TestCase

from utils import run_test_and_get_output, check_output


class TestTask(TestCase):

    def test_task(self):

        check_output("hello world\n")

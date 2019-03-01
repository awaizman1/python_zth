
from unittest import TestCase

from utils import check_output


class TestTask(TestCase):

    def test_task(self):

        check_output("""[34, 15]
sample is 12, avg is 11.0
True
sample is 10, avg is 11.0
False
""")


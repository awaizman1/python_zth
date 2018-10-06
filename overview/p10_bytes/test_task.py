from unittest import TestCase

from utils import check_samples, check_output


class TestTask(TestCase):

    def test_task(self):

        check_output("""Very good!
It seems you are now mastering python bytes.
Did you solve this without working on immutable str?
If not try again...
""")

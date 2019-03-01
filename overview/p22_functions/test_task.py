import re
from unittest import TestCase

from utils import run_test_and_get_output


class TestTask(TestCase):

    def test_task(self):

        output = run_test_and_get_output(None, True)

        self.assertEqual(output.count("running foo on (1, 2) in thread"), 3)
        tids = re.findall("thread \d+", output)
        self.assertEqual(3, len(tids))
        self.assertFalse(all(tid == tids[0] for tid in tids))


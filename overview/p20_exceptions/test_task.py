from unittest import TestCase

from utils import run_test_and_get_output


class TestTask(TestCase):

    def test_task(self):
        output = run_test_and_get_output(None)
        self.assertNotIn("RedisKeyNotFoundError", output, "Not good - redis still appears in output...")

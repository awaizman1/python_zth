from unittest import TestCase

from utils import check_samples, check_output


class TestTask(TestCase):

    def test_task(self):

        check_output("nohtyp morf orez ot oreh\n")


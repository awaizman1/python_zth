from unittest import TestCase

from utils import check_samples


class TestTask(TestCase):

    def test_task(self):
        samples = [
            ("5\n0", "Enter diagonal:\n  *  \n *** \n*****\n *** \n  *  \n"
                     "Enter diagonal:\n"),
            ("1\n0", "Enter diagonal:\n*\n"
                     "Enter diagonal:\n"),
            ("5\n3\n0", "Enter diagonal:\n  *  \n *** \n*****\n *** \n  *  \n"
                        "Enter diagonal:\n"
                        " * \n***\n * \n"
                        "Enter diagonal:\n")
        ]

        check_samples(samples)

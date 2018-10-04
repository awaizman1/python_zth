from unittest import TestCase

from utils import check_samples


class TestTask(TestCase):

    def test_task(self):

        samples = [
            ('1aA#$', f"Enter password:\n'1aA#$' is invalid\n"),  # min length
            ('1aA#1aA#1aA#1aA#1', f"Enter password:\n'1aA#1aA#1aA#1aA#1' is invalid\n"),  # max length
            ('1aa#1a', f"Enter password:\n'1aa#1a' is invalid\n"),  # no uppercase
            ('1AA#1A', f"Enter password:\n'1AA#1A' is invalid\n"),  # no lowercase
            ('aA#bB$', f"Enter password:\n'aA#bB$' is invalid\n"),  # no digit
            ('aA12bB', f"Enter password:\n'aA12bB' is invalid\n"),  # no special
            ('1qaz@W', f"Enter password:\n'1qaz@W' is valid\n"),
            ('passW0rd$', f"Enter password:\n'passW0rd$' is valid\n")
        ]

        check_samples(samples)

from unittest import TestCase

from utils import check_output


class TestTask(TestCase):

    def test_task(self):

        check_output("""10
2
16
1
121
bool(0) is False --> good!
bool(12) is True --> good!
bool(0.0) is False --> good!
bool(-1.5) is True --> good!
bool([]) is False --> good!
bool([1, 2]) is True --> good!
bool() is False --> good!
bool(False) is True --> good!
bool(None) is False --> good!
conn is closed, opening...
conn is now open
""")

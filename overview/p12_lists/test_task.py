from unittest import TestCase

from utils import check_samples, check_output


class TestTask(TestCase):

    def test_task(self):

        check_output("""[10, 11, 12]
[1, 2, 3, 4, 5, 6]
[('Max', 76), ('Tal', 96), ('Jhon', 100), ('Bob', 88)]
[[18, 21, 24], [27, 30, 33], [36, 39, 42]]
""")

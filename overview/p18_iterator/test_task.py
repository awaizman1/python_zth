from unittest import TestCase

from utils import check_output


class TestTask(TestCase):

    def test_task(self):

        check_output("""Dave :  78
Shirley :  95
Lena :  92
Jhon :  56
Dave :  78
Shirley :  95
Lena :  92
Jhon :  56
""")

from unittest import TestCase

from utils import check_output


class TestTask(TestCase):

    def test_task(self):

        check_output("""['Dave', 'Elthon', 'Jessy', 'Jhon', 'Lena', 'Mark', 'Mike', 'Neli', 'Shira']
['Dave', 'Elthon', 'Jessy', 'Mark']
['Jhon', 'Lena', 'Mike', 'Neli', 'Shira']
""")

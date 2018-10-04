from unittest import TestCase

from utils import check_output


class TestTask(TestCase):

    def test_task(self):

        check_output("""<class 'int'>
<class 'bool'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'dict'>
where the hell this line came from?
student jhon is male
""")

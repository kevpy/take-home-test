from problem_1 import str_transform
from problem_2 import chunk_string


# test function for problem 1
def test_problem_1():
    assert str_transform('abcde') == 'zyxwv'


def test_problem_2():
    test_text = 'Simple text'
    length = 4
    assert chunk_string(test_text, length) == ['Simp', 'le t', 'ext']

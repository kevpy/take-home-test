from problem_1 import str_transform
from problem_2 import chunk_string
from problem_3 import temp_example


# test function for problem 1
def test_problem_1():
    assert str_transform('abcde') == 'zyxwv'


def test_problem_2():
    test_text = 'Simple text'
    length = 4
    assert chunk_string(test_text, length) == ['Simp', 'le t', 'ext']


def test_problem_3():
    timestamp = [1, 2, 3, 4, 5, 6, 7]
    temperature_reading = [9, 2, 3, 5, 8, 1, 10]
    threshold = 4
    assert list(
        temp_example(timestamp, temperature_reading, threshold)) == [4, 7]

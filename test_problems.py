from problem_1 import str_transform
from problem_2 import chunk_string
from problem_3 import temp_example
from problem_4 import stock_analyst


# test for problem 1
def test_problem_1():
    assert str_transform('abcde') == 'zyxwv'


# test for problem 2
def test_problem_2():
    test_text = 'Simple text'
    length = 4
    assert chunk_string(test_text, length) == ['Simp', 'le t', 'ext']


# test for problem 3
def test_problem_3():
    timestamp = [1, 2, 3, 4, 5, 6, 7]
    temperature_reading = [9, 2, 3, 5, 8, 1, 10]
    threshold = 4
    assert list(
        temp_example(timestamp, temperature_reading, threshold)) == [4, 7]


# test for problem 4
def test_problem_4():
    P = [30, 20, 10, 15, 17, 25, 20, 23]
    assert stock_analyst(P) == [2, 5]

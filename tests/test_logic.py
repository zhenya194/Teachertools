from teachertools import average_mark

def test_average_mark():
    assert average_mark(10, 5) == 7.5
def test_average_mark():
    assert average_mark(5, 5, 5) == 5
def test_average_mark():
    assert average_mark(2) == 2
def test_average_mark():
    assert average_mark(3.5, 7, 11, 4.5) == 6.5

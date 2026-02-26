from teachertools import average_mark, is_enter

def test_average_mark():
    assert average_mark(10, 5) == 7.5
def test_average_mark():
    assert average_mark(5, 5, 5) == 5
def test_average_mark():
    assert average_mark(2) == 2
def test_average_mark():
    assert average_mark(3.5, 7, 11, 4.5) == 6.5

def test_is_enter():
    assert is_enter(5, 10, 5) == 2
def test_is_enter():
    assert is_enter(5, 5, 5) == 2
def test_is_enter():
    assert is_enter(7, 5.5, 10, 3, 4.5, 6) == 1
def test_is_enter():
    assert is_enter(6, 12, 10, 1, 4, 7, 4) == 3

print('hello pytest')
import pytest
import sys


def test_hello():
    print("hello world!")
    assert 1


@pytest.mark.xfail()
def test_yoyo1():
    a = "hello"
    b = "hello world"
    assert a == b


@pytest.mark.xfail()
def test_yoyo2():
    a = "hello"
    b = "hello world"
    assert a != b


if __name__ == '__main__':
    # pytest.main(['-q','test_*.py'])
    pytest.main(['-s', 'test_*.py'])

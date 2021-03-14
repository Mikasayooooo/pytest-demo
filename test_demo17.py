print('hello pytest')
import pytest
import sys


@pytest.mark.webtest
def test_send_http():
    print("mark web test")


def test_something_quick():
    pass


def test_another():
    pass


@pytest.mark.hello
class TestClass:
    def test_01(self):

        print("hello :")

    def test_02(self):

        print("hello world!")


if __name__ == '__main__':
    # pytest.main(['-q','test_*.py'])
    pytest.main(['-s', 'test_*.py','-m=webtest'])

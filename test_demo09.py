print('hello pytest')
import pytest
import sys


@pytest.mark.webtest
def test_send_http():
    pass # perform some webtest test for your app

def test_something_quick():
    pass

def test_another():
    pass


class TestClass:
    def test_method(self):
        pass


if __name__ == '__main__':
    # pytest.main(['-q','test_*.py'])
    # pytest.main(['-s','test_*.py'])
    # pytest.main(["-s", "test*.py", "-m=not webtest"])
    # pytest.main(["-s", "test*.py", "-m=webtest"])

    # -v 指定的函数节点 id
    # pytest.main(["-v","test_demo09.py::TestClass::test_method"])
    # pytest.main(["-v", "test*.py::TestClass",
    #              "test*.py::test_send_http"])
    pytest.main('-v" test_demo09.py::TestClass::test_method')
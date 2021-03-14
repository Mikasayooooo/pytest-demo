print('hello pytest')
import pytest
import sys

class TestClass1:


    def test_s1(self,login):
        print("用例 1：登录之后其它动作 111")

    def test_s2(self):  # 不传 login
        print("用例 2：不需要登录，操作 222")

    def test_s3(self,login):
        print("用例 3：登录之后其它动作 333")

if __name__ == '__main__':
    # pytest.main(['-q','test_*.py'])
    pytest.main(['-s','test_*.py'])
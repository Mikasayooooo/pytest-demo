'''
versioninfo:1.1
'''

print('hello pytest')
import pytest
import sys


class TestClass1:

    def test_zero_division(self):
        '''断言异常'''
        with pytest.raises(ZeroDivisionError) as excinfo:
            1 / 0

        # 断言异常类型 type
        assert excinfo.type == ZeroDivisionError
        # 断言异常 value 值
        assert "division by zero" in str(excinfo.value)

    def is_true(self,a):
        if a > 0:
            return True
        else:
            return False

    def test_01(self):
        '''断言 xx 为真'''
        a = 5
        b = -1
        assert self.is_true(a)
        assert not self.is_true(b)

    def test_02(self):
        '''断言 b 包含 a'''

        a = "hello"
        b = "hello world"
        assert a in b

    def test_03(self):
        '''断言相等'''
        a = "yoyo"
        b = "yoyo"
        assert a == b

    def test_04(self):
        '''断言不等于'''
        a = 5
        b = 6
        assert a != b


if __name__ == '__main__':
    # pytest.main(['-q','test_*.py'])
    pytest.main(['-s','test_*.py'])
print('hello pytest')
import pytest
import sys


def setup_module(self):
    print('***************************')
    print(sys._getframe().f_code.co_name) #内部获取函数或方法名


def teardown_module(self):
    print('***************************')
    print(sys._getframe().f_code.co_name)


def setup_function(self):
    print('***************************')
    print(sys._getframe().f_code.co_name)


def teardown_function(self):
    print('***************************')
    print(sys._getframe().f_code.co_name)

def test_two():
    a = 'aa'
    b = 'bb'
    assert a not in b


class TestClass1:
    '''
    观察执行顺序
    用例是按照顺序执行
    '''

    def setup(self):
        print('***************************')
        print(sys._getframe().f_code.co_name)

    def teardown(self):
        print('***************************')
        print(sys._getframe().f_code.co_name)

    def setup_class(self):
        print('***************************')
        print(sys._getframe().f_code.co_name)

    def teardown_class(self):
        print('***************************')
        print(sys._getframe().f_code.co_name)

    def setup_method(self):
        print('***************************')
        print(sys._getframe().f_code.co_name)

    def teardown_method(self):
        print('***************************')
        print(sys._getframe().f_code.co_name)

    def test_one(self):
        a = 'aa'
        b = 'bb'
        assert a not in b

    # def test_two(self):
    #     d = {'name':'lhl'}
    #     assert hasattr(d,'name')
    #
    # def test_three(self):
    #     a = 'aa'
    #     b = 'bb'
    #     assert a in b

    # def test_c(self):
    #     a = 'aa'
    #     b = 'bb'
    #     assert a in b
    #
    # def test_a(self):
    #     a = 'aa'
    #     b = 'bb'
    #     assert a in b
    #
    # def test_b(self):
    #     a = 'aa'
    #     b = 'bb'
    #     assert a in b


# class TestClass2:
#
#     def setup(self):
#         print('***************************')
#         print(sys._getframe().f_code.co_name)
#
#     def teardown(self):
#         print('***************************')
#         print(sys._getframe().f_code.co_name)
#
#     def setup_module(self):
#         print('***************************')
#         print(sys._getframe().f_code.co_name)
#
#     def teardown_module(self):
#         print('***************************')
#         print(sys._getframe().f_code.co_name)
#
#     def setup_function(self):
#         print('***************************')
#         print(sys._getframe().f_code.co_name)
#
#     def teardown_function(self):
#         print('***************************')
#         print(sys._getframe().f_code.co_name)
#
#     def setup_class(self):
#         print('***************************')
#         print(sys._getframe().f_code.co_name)
#
#     def teardown_class(self):
#         print('***************************')
#         print(sys._getframe().f_code.co_name)
#
#     def setup_method(self):
#         print('***************************')
#         print(sys._getframe().f_code.co_name)
#
#     def teardown_method(self):
#         print('***************************')
#         print(sys._getframe().f_code.co_name)
#
#     def test_one(self):
#         a = 'aa'
#         b = 'bb'
#         assert a not in b

if __name__ == '__main__':
    # pytest.main(['-q','test_*.py'])
    pytest.main(['-s','test_*.py'])
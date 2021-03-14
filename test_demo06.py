print('hello pytest')
import pytest
import sys


class TestClass1:

    def setup(self):
        print(sys._getframe().f_code.co_name)
        # raise NameError  # 模拟异常
        '''
        2.如果在 setup 就异常了，那么是不会去执行 yield 后面的teardown 内容了
        '''

    def test_s1(self):
        print("用例 1：搜索 python-1")
        # 如果第一个用例异常了，不影响其他的用例执行
        raise NameError  # 模拟异常

    def test_s2(self,open):  # 不传 login
        print("用例 2：搜索 python-2")

    @pytest.mark.usefixtures('open')
    def test_s3(self):
        print("用例 3：搜索 python-3")


    # parametrize 的第一个参数与test_eval一致
    @pytest.mark.parametrize("test_input,expected",
                             [("3+5", 8),
                              ("2+4", 6),
                              pytest.param("6 * 9", 42,marks=pytest.mark.xfail)
                              ])
    def test_eval(self,test_input, expected):
        assert eval(test_input) == expected


    @pytest.mark.parametrize('x',[1,2])
    @pytest.mark.parametrize('y',[3,4])
    def test_foo(self,x,y):
        # print(("测试数据组合：x->%s, y->%s" % (x, y)))
        print((f"测试数据组合：x->{x}, y->{y}" ))
        print(f'x + y = {x+y}')



if __name__ == '__main__':
    # pytest.main(['-q','test_*.py'])
    pytest.main(['-s','test_*.py'])
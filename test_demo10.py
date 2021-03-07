print('hello pytest')
import pytest
import sys

canshu = [{"user": "amdin", "psw": "111"}]

@pytest.fixture(scope="module")
def login2(request):

    user = request.param["user"]
    psw = request.param["psw"]
    print("正在操作登录，账号：%s, 密码：%s" % (user, psw))
    if psw:
        return True
    else:
        return False


@pytest.mark.parametrize("login2", canshu, indirect=True)
class Test_xx():

    def test_01(self, login2):

        '''用例 1 登录'''
        result = login2
        print("用例 1：%s" % result)
        assert result == True

    def test_02(self, login2):

        result = login2
        print("用例 3,登录结果：%s" % result)
        if not result:
            pytest.xfail("登录不成功, 标记为 xfail")

        assert 1 == 1


    def test_03(self, login2):

        result = login2
        print("用例 3,登录结果：%s" % result)
        if not result:
            pytest.xfail("登录不成功, 标记为 xfail")

        assert 1 == 1



if __name__ == '__main__':
    # pytest.main(['-q','test_*.py'])
    pytest.main(['-s', 'test_*.py'])

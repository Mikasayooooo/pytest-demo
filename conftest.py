import pytest

'''
conftest.py 配置需要注意以下点：
conftest.py 配置脚本名称是固定的，丌能改名称
conftest.py 不运行的用例要在同一个 pakage 下，并且有
__init__.py 文件
不需要 import 导入 conftest.py，pytest 用例会自动查找
'''

'''
:arg scope: scope 有四个级别参数 "function" (默讣), "class",
"module" or "session".

:arg params: 一个可选的参数列表，它将导致多个参数调用
fixture 功能呾所有测试使用它

:arg autouse: 如果为 True，则为所有测试激活 fixture func 可
以看到它。 如果为 False（默讣值）则显式需要参考来激活 fixture

 :arg ids: 每个字符串 id 的列表，每个字符串对应于 params 返样
他们就是测试 ID 的一部分。 如果没有提供 ID 它们将从 params 自动
生成

 :arg name: fixture 的名称。 返默讣为装饰函数的名称。 如果
fixture 在定义它的同一模块中使用，夹具的功能名称将被请求夹具的
功能 arg 遮蔽; 解决返个问题的一种方法是将装饰函数命名
'''

@pytest.fixture()
def login():
    print('输入账号，密码先登录')

@pytest.fixture(scope='module')
def open():
    print('打开浏览器')

    yield
    print("执行 teardown!")
    print("最后关闭浏览器")


# @pytest.fixture(scope='module')
# def open2(request):
#     print('打开浏览器')
#
#     def close():
#         request.addfinalizer(close)
#         # yield
#         print("执行 teardown2!")
#         print("最后关闭浏览器2")
#     return open2


@pytest.fixture(scope='module',autouse=True)
def doc():
    print('文档说明开始')

    yield
    print("执行 teardown!")
    print("文档说明结束")


@pytest.fixture(scope="module")
def login2(request):

    user = request.param["user"]
    psw = request.param["psw"]
    print("正在操作登录，账号：%s, 密码：%s" % (user, psw))
    if psw:
        return True
    else:
        return False



def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="myoption: type1 or type2")


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")




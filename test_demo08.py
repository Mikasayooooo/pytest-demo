print('hello pytest')
import pytest
import sys


# import test_demo7
# minversion = pytest.mark.skipif(test_demo7.__versioninfo__ <
# (1,1),
# reason="at least mymodule-1.1 required")


class TestClass1:


    @pytest.mark.skip(reason="no way of currently testing this")
    def test_the_unknown(self):
        pass

    @pytest.mark.skipif(sys.version_info<=(3,7,9),reason='python version低于3.7.9跳过此用例')
    def test_function(self):
        # if not valid_config():
        # pytest.skip("unsupported configuration")
        print(sys.version_info)
        pytest.skip('reason',allow_module_level = True)

    # def test_skip(self):
    #     if not pytest.config.getoption("--custom-flag"):
    #         pytest.skip("--custom-flag is missing, skipping tests",
    #                     allow_module_level=True)

    # @minversion
    # def test_11(self):
    #     pass
    #
    # @minversion
    # def test_22(self):
    #     pass

    @pytest.mark.skipif(sys.platform == 'win32',
                        reason="does not run on windows")
    class TestPosixCalls(object):
        def test_function(self):
            "will not be setup or run under 'win32' platform"

            print(sys.platform)

    '''
    1.无条件地跳过模块中的所有测试：
    pytestmark = pytest.mark.skip("all tests still WIP")
    
    2.根据某些条件跳过模块中的所有测试
    pytestmark = pytest.mark.skipif(sys.platform == "win32","tests for linux→ only"
    
    3.如果缺少某些导入，则跳过模块中的所有测试
    pexpect = pytest.importorskip("pexpect")
    '''


if __name__ == '__main__':
    # pytest.main(['-q','test_*.py'])
    pytest.main(['-s','test_*.py'])
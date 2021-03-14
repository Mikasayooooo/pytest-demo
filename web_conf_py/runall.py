import pytest
import os
import sys
import re


def find_files(sPath):
    '''读取指定文件夹下的所有test_*.py文件'''
    fileList = []
    for s_child in os.listdir(sPath):
        if os.path.isdir(s_child):
            find_files(s_child)
        elif s_child.startswith('test_') and s_child.endswith('.py'):
            fileList.append(s_child)
            # print(s_child)
    if fileList:
        for file in fileList:
            print(file) # 不能直接return


if __name__ == '__main__':
    '''测试用例执行顺序'''
    # pytest.main(['-v'])
    # pytest.main(['-v','baidu/test_2.py'])
    # pytest.main(['-v','baidu/test_2.py::test_06'])
    # 7 passed in 7.10s


    '''当前文件的文件名'''
    # print(os.path.basename(__file__))
    # print(os.path.basename(sys.argv[0]))


    # find_files('D:\_root\study\workspace\projects\pytest_study\web_conf_py')


    '''多cpu并行执行用例，直接加个-n参数即可，后面num参数就是并行数量，比如num设置为3
    pip install pytest-xdist '''
    # pytest.main(['-n','2']) #  7 passed in 4.63s
    # pytest.main(['-n', '4'])  # 7 passed in 2.82s
    # pytest.main(['-n', '8'])    #7 passed in 2.28s


    '''pytest baidu/test_1_baidu.py -s --count=5
    加上参数--count=5，用例会重复执行5次'''
    # pytest.main(['-v','--count','5'])    #35 passed in 35.19s
    # pytest.main(['-v', '--count', '5','-n','8']) #35 passed in 6.40s
    # pytest.main(['-v'])

    '''allure报告生成'''
    pytest.main(['--alluredir','./report/allure_raw'])
    os.system('allure serve report/allure_raw')
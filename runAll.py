import pytest
import os

# path = os.path.dirname(__file__)
# print(path)
# path = path + "/report/"
# path = "./report"
pytest.main(["-s", "--alluredir=./report","--clean-alluredir"])  # 运行 所有测试用例,生成json文件

os.system("allure  generate report/ -o report/html --clean")
# result = os.system(f"allure serve ./report")
# print(f"result=./report")
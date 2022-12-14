import os

import pytest, yaml,allure
from allure_commons._allure import story, feature, step

from page.app import APP


@feature('搜索模块')
class TestSearch:
    @pytest.mark.parametrize("key,price",
                             yaml.safe_load(open('F:\\PythonCoding\\xueqiuAutoTest\\Testdata\\search.yml')))
    @story('搜索框搜索公司股价')
    def test_search001(self, key, price):
        with step('1、首页点击搜索框，进入搜索页面，输入关键词进行搜索，并断言'):
            assert APP().start().main().goto_search_page().searchinput(key).get_price() > float(price)

    @story('点击头像进入我的页面')
    def test_photo001(self):
        APP().start().main().goto_my_photo()


# if __name__ == '__main__':
#     dripath = 'F:\\pythoncoding\\xueqiuAutoTest\\Testreport\\Allure_report'
#     pytest.main('./xueqiuTestCase/test_search.py', '-sv', "--alluredir", dripath)
#     os.system(f"allure generate {dripath} -o {dripath} --clean")
#     os.system('allure generate ../Testreport/Allure_report -o  ../Testreport/Allure_report --clean')

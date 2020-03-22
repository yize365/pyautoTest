import sys
from time import sleep
import pytest
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.baidu_page import BaiduPage
class TestSearch:
    """百度搜索"""

    def test_baidu_search_case(self, browser, base_url):
        """
        名称：百度搜索"pytest"
        步骤：
        1、打开浏览器
        2、输入"pytest"关键字
        3、点击搜索按钮
        检查点：
        * 检查页面标题是否包含关键字。
        """
        page = BaiduPage(browser)
        page.get(base_url)
        page.search_input = "pytest"
        page.search_button.click()
        sleep(2)
        assert browser.title == "pytest_百度搜索"
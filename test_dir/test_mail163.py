import sys
from time import sleep
import pytest
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
from page.mail163_page import Mail163_Page

file_path=abspath('../data/')
upload_page='file:///'+file_path+'upfile.html'

class TestLogin:
    """百度搜索"""
    def test_163_login_case(self, browser, base_url):
        """
            1.打开浏览器
            2.点击密码登录
            3.进入iframe
            4.输入账户
            5.输入密码
            6.点击登陆
            7.判断是否登录成功
        """
        login = Mail163_Page(browser)
        login.get(base_url)
        login.search_mmdl_btn.click()
        browser.switch_to.frame(login.search_frame)
        login.search_name_input="yitianshi2012"
        login.search_pwd_input="lzw@19900102"
        login.search_login_btn.click()
        sleep(3)
        assert login.search_is_login.text == "退出"
        """
        1.点击写信
        2.输入收件人
        3.输入主题
        4.添加附件
        5.切换表单
        6.输入文本内容
        7.
        """
        login.search_xx_btn.click()
        login.search_sjr_btn.send_keys('1558570566@qq.com')
        login.search_zt_btn.send_keys('测试下右键是否畅通')
        browser.get(upload_page)
        login.search_tjfj_btn.send_keys(file_path+'163.txt')
        browser.switch_to.frame(login.search_frame_edit)
        login.search_bj_btn.sendk_keys('这里是输入的文件内容')
        browser.switch_to.default_content()
        login.search_send_btn.click()
        assert login.search_is_send_sucess == '返回收件箱'


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_mail163.py"])
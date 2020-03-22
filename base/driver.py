# @File  : driver.py
# @Author: yize365
# @Date  :  2020/02/22
# @Function:
# @Remarks:
from selenium import webdriver
import page
class GetDriver:
    #设置类属性
    driver=None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            #实例化浏览器
            cls.driver=webdriver.Firefox()
            #最大化
            cls.driver.maximize_window()
            #打开浏览器
            cls.driver.get(page.url)
        return cls.driver

    #退出driver
    @classmethod
    def quit_diver(cls):
        if cls.driver:
            cls.driver.quit()
            #注意需要置空
            cls.driver=None
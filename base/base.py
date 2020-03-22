from selenium.webdriver.support.wait import WebDriverWait
import time
from tools.get_log import Get_Log
log=Get_Log.get_log("页面操作log.log")

class Base:
    #初始化
    def __init__(self,driver):
        log.info("初始化driver{}".format(driver))
        self.driver=driver

    #查找元素方法|
    def base_find_element(self, loc, timeout=30, poll=0.5):
        log.info("正在查找元素:{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_element(*loc))

    #查找一组元素
    def base_find_elements(self,loc,timeout=30,poll=0.5):
        log.info("正在查找元素组:{}".format(loc))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    #点击方法
    def base_click(self,loc):
        log.info("正在点击元素:{}".format(loc))
        self.base_find_element(loc).click()

    #输入方法
    def base_input(self,loc,value):
        log.info("正在查找元素:{}".format(loc))
        ele=self.base_find_element(loc)
        #清空
        log.info("正在给元素:{}清空".format(loc))
        ele.clear()
        #输入
        log.info("正在给元素:{}输入内容".format(value))
        ele.send_keys(value)

    #获取文本方法
    def base_get_text(self,loc):
        #注意:一定要返回元素的文本信息
        log.info("正在获取元素:{}文本".format(loc))
        return self.base_find_element(loc).text

    #获取value属性的方法封装
    def base_get_value(self,loc):
        log.info("正在获取元素:{}的value属性".format(loc))
        return self.base_find_element(loc).get_attribute("value")

    #截图方法
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    #判断元素是否存在(使用情况举例:测试用例登陆成功之后判断)
    def base_if_exist(self,loc):
        try:
            log.info("判断元素{}存在".format(loc))
            self.base_find_element(loc,timeout=2)
            #找到元素
            return True
        except:
            #未找到元素
            log.info("判断元素{}不存在".format(loc))
            return False
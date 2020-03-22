# 这里放置测试需要的元素定位数据
from selenium.webdriver.common.by import By
url="http://www.baidu.com"
"""
百度搜索定位元素
"""
search_input_ele = By.ID,"kw"
search_button_ele =By.ID,"su"
settings_ele = By.LINK_TEXT,"设置"
search_setting_ele = By.CSS_SELECTOR,".setpref"
save_setting_ele = By.CSS_SELECTOR,".prefpanelgo"
# 定位一组元素
search_result_ele = By.XPATH,"//div/h3/a"

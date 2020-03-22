# from poium import Page, PageElement, PageElements
from base.base import Base
import page
class BaiduPage(Base):
    # search_input = PageElement(id_="kw", describe="搜索框")
    # search_button = PageElement(id_="su", describe="搜索按钮")
    # settings = PageElement(link_text="设置", describe="设置下拉框")
    # search_setting = PageElement(css=".setpref", describe="搜索设置选项")
    # save_setting = PageElement(css=".prefpanelgo", describe="保存设置")
    # # 定位一组元素
    # search_result = PageElements(xpath="//div/h3/a", describe="搜索结果")
    def search_input(self,data):
        Base.base_input(self,page.search_input_ele,data)

    def search_button(self):
        Base.base_click(self,page.search_button_ele)

    def settings(self):
        Base.base_click(self, page.settings_ele)

    def search_setting(self):
        Base.base_click(self, page.search_setting_ele)

    def save_setting(self):
        Base.base_click(self, page.save_setting_ele)

    # 定位一组元素
    def search_result(self):
        Base.base_find_elements(self,page.search_result_ele)
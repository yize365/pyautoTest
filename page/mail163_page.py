from poium import Page, PageElement, PageElements

class Mail163_Page(Page):
    search_mmdl_btn=PageElement(id_="switchAccountLogin", describe="密码登录")
    search_frame=PageElement(css='iframe[id^="x-URS-iframe"]', describe="切换表单")
    search_name_input=PageElement(name="email", describe="账号输入框")
    search_pwd_input=PageElement(name="password", describe="密码输入框")
    search_login_btn=PageElement(id_="dologin", describe="登陆按钮")
    search_is_login=PageElement(link_text="退出", describe="退出按钮")

    #写信传附件
    search_xx_btn=PageElement(id_="_mail_component_19_19",describe="写信按钮")
    search_sjr_btn=PageElement(id_="_mail_emailtips_0_223",describe="收件人输入")
    search_zt_btn=PageElement(id_="1584696266952_subjectInput",describe="主题输入")
    search_tjfj_btn=PageElement(id_="1584783495020_attachBrowser",describe="添加附件")
    search_frame_edit = PageElement(css='iframe[class="APP-editor-iframe"]', describe="切换表单")
    search_bj_btn=PageElement(id_="_mail_component_229_229",describe="编辑输入")
    search_send_btn=PageElement(xpath="//*[@id='_mail_button_8_201']/span[2]",describe="点击发送")
    search_is_send_sucess=PageElement(xpath="//*[contains(@text,'返回收件箱')]",describe="返回收件箱")
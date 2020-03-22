import yagmail
def send_email(filename):
    filepath="../report/"+filename
    #链接邮箱服务器
    yag=yagmail.SMTP(user="lzw1558570566@126.com",
                     password="IPCMJWZWMKVJXKNN",
                     host="smtp.126.com")
    subject="主题,自动化测试报告"
    #邮件正文
    contents=['这是邮件正文,为了测试邮件可否正常发送!']
    #发送邮件
    yag.send(['1558570566@qq.com'],'subject',contents,[filepath])
    print('email has send out!')
    #如果想给多个人发邮件,就需要将人员列表放进list
    #如果想发附件,只需要指定本地附件路径即可

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr
#发送邮件主题
subject='Python send email test'

#发送附件类型的邮件--必须设置from 和 to
with open('../report/log.txt','rb') as f:
    send_att=f.read()
att = MIMEText(send_att,'text','utf-8')
att["Content-Type"] = 'application/octet-stream '
att["Content-Disposition"] = 'attachment;filename="log.txt"'
msg = MIMEMultipart()
msg['From'] = formataddr(["yize365", 'lzw1558570566@126.com'])
msg['To'] = formataddr(["yize", '1558570566@qq.com'])
msg['Subject'] = subject
msg.attach(att)

# #编写HTML类型的邮件正文--发送文本类型
# msg['From'] = formataddr(["yize365", 'lzw1558570566@126.com'])
# msg['To'] = formataddr(["yize", '1558570566@qq.com'])
# msg = MIMEText('<html><h1>你好!</h1></html>','html','utf-8')
# msg['Subject'] = Header(subject,'utf-8')

#发送邮件
smtp = smtplib.SMTP()
try:
    smtp.connect("smtp.126.com")
    smtp.login("lzw1558570566@126.com","IPCMJWZWMKVJXKNN")
    smtp.sendmail('lzw1558570566@126.com', ['1558570566@qq.com'], msg.as_string())
except:
    print("login failed")
smtp.quit()

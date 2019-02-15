#发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText


#SMTP服务器
SMTPServer = "smtp.163.com"
#发邮件的地址
sender = "18332726983@163.com"
#发送者邮箱密码
passwd = "74108520a"



#设置发送的内容
message = "aaaaaaa"
#转换成邮件文本
msg = MIMEText(message)

#主题
msg["Subject"] = "一封信"
#发送者
msg["From"] = sender


#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer, 25)

#登录邮箱
mailServer.login(sender, passwd)
#发送邮件
mailServer.sendmail(sender, ["18332726983@163.com"], msg.as_string())
#退出邮箱
mailServer.quit()







import smtplib
from email.mime.text import MIMEText
import socket#获取计算机名称
email_sender='2359618581@qq.com'
email_receiver=['845765697@qq.com']
sqm='ygprzjfeatxlebfh'
hostname=socket.gethostname()#获取本机IP
while True:
    ip=socket.gethostbyname(hostname)
    print(ip)
    if ip != '127.0.0.1':
        break
print('*'*50)
print(ip)

msg=MIMEText(ip,'plain','utf-8')
msg['Subject']='树莓派IP地址'
msg['From']=email_sender
connectiong=smtplib.SMTP('smtp.qq.com',25)
connectiong.login(email_sender,sqm)
connectiong.sendmail(email_sender,email_receiver,msg.as_string())
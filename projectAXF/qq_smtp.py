import smtplib
from email.mime.text import  MIMEText

msg = MIMEText('hello python now i am coming')
from_addr = '1640191389@qq.com'
from_pwd ='hbftrbzffzbqefjf'

to_addr = '18330016979@163.com'
smtp_srv = 'smtp.qq.com'
try:
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
    print(e)
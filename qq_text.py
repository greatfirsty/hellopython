from email.mime.text import MIMEText
from email.mime.multipart import MIMEBase,MIMEMultipart
email_mul = MIMEMultipart()
mail_text = MIMEText('hello i am coming ','plain','utf-8')
email_mul.attach(mail_text)
with open('02.html','rb')as f:
    s = f.read()
    m = MIMEText(s,'base64','utf-8')
    m['Content-Type'] = 'application/octet-stream'
    m['Content-Disposition'] = "attachment;filename='02.html'"
    email_mul.attach(m)
from_addr = '1640191389@qq.com'
from_pwd = 'hbftrbzffzbqefjf'

to_addr = '18330016979@163.com'
smtp_srv = 'smtp.qq.com'
try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr,[to_addr],email_mul.as_string())
    srv.quit()
except Exception as e:
    print(e)
#添加邮件头
mail['from']表示
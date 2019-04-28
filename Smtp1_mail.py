from email.mime.text import MIMEText
mail_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>这是一封HTML格式邮件</title>
</head>
<body>
<h1>hello i am coming</h1>
</body>
</html>
'''
msg = MIMEText(mail_content,'html','utf-8')
from_addr = '1640191389@qq.com'
from_pwd = 'hbftrb'

to_addr = '18330016979@163.com'
smtp_srv = 'smtp.qq.com'
try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr,[to_addr],msg.as_string())
    srv.quit()
except Exception as e:
  print(e)

from email.mime.multipart import MIMEMultipart
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
#msg = MIMEText(mail_content,'html','utf-8')
#发送附件
send_file = open(r"C:\\Users\hss\workgit\hellopython\Test Results - Twisted_Trial_for_test_baidu_My_Test_test_baidu.html",'rb').read()
att = MIMEText(send_file,'base64','utf-8')
att['content-Type'] = 'application/octet-stream'
att['content-Disposition'] = 'attachment;filename="log.txt"'
#这里主要是对附件的格式
msgrot = MIMEMultipart('related')
subject = '发送测试报告'
msgrot['Subject'] = subject
msgrot.attach(att)

from_addr = '1640191389@qq.com'
from_pwd = 'goinknvgbiz'#授权码
to_addr = '18330016979@163.com'
smtp_srv = 'smtp.qq.com'

try:
    import smtplib
    srv = smtplib.SMTP_SSL(smtp_srv.encode(),465)
    srv.login(from_addr,from_pwd)
    srv.sendmail(from_addr,[to_addr],msgrot.as_string())


    srv.quit()
except Exception as e:
  print(e)

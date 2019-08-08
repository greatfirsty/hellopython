import smtplib
import unittest

import time
from email.mime.text import MIMEText
from email.header import Header

import os
from HtmlTestRunner import HTMLTestRunner
test_dir = '../test_project/test_case'
discovery = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

def send_mail(file_new):
    f = open(file_new,'rb')
    mail_body = f.read()
    msg = MIMEText(mail_body,'html','utf-8')
    msg['subject']= Header('自动化测试报告')

    from_addr = '1640191389@qq.com'
    from_pwd = 'qeovdiqqtpycjege'  # 授权码
    to_addr = '18330016979@163.com'
    smtp_srv = 'smtp.qq.com'
    try:

        srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465)
        srv.login(from_addr, from_pwd)
        srv.sendmail(from_addr, [to_addr], msg.as_string())

        srv.quit()
    except Exception as e:
        print(e)

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport,lists[-1])
    return file_new


if __name__ == '__main__':
    report_dir = r'C:\Users\hss\workgit\hellopython\test_project\reports'
    now = time.strftime('%Y_m_d %H_%M_%S')
    filename =test_dir+ './'+now + 'result.html'
    fp = open(filename,'w')
    runner = HTMLTestRunner(stream=fp,report_title='测试报告',descriptions='用例执行情况')
    runner.run(discovery)
    fp.close()
    new_reports = new_report(report_dir)
    send_mail(new_reports)


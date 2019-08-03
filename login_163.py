import time
from selenium import webdriver
def login():
    dr = webdriver.Chrome()
    #打开登陆163邮箱的网页
    dr.get('http://mail.163.com/')
    #将浏览器窗口最大化
    dr.maximize_window()
    #找到邮箱账号登录框对应的iframe
    dr.find_element_by_xpath(" // *[ @ id = 'lbNormal']").click()
    #这里选中提交框
    aa = dr.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
    #将操作转向提交框
    dr.switch_to.frame(aa)

    #将自己的邮箱地址输入到邮箱账号框中
    email = dr.find_element_by_name('email')
    email.send_keys('18330016979')
    #找到密码输入框
    password = dr.find_element_by_name('password')
    password.send_keys('hansaisai123')
    #找到登陆按钮
    login_btn = dr.find_element_by_id('dologin')
    #点击登陆按钮
    login_btn.click()
    #等待10秒看是否登陆成功
    time.sleep(10)

if __name__ == '__main__':
    login()
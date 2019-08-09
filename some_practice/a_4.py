from threading import Thread
from time import ctime, time, sleep

from selenium import webdriver


def test_baidu(browser,search):
    print('start : {}'.format(ctime()))
    print('browser : {}'.format(browser))
    driver = ''
    if browser == 'ie':
        driver = webdriver.Ie()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == 'ff':
        driver = webdriver.Firefox()
    else:
        print('参数有误')
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys(search)
    driver.find_element_by_id('su').click()
    sleep(5)
    driver.quit()
if __name__ == '__main__':

    dicts={
        'chrome':'美男',
        'ie':'好汉歌',
        'ff':'python'

    }
    threads = []
    files = range(len(dicts))
    for k,v in dicts.items():
        t = Thread(target=test_baidu,args=(k,v))
        threads.append(t)
    for i in files:
        threads[i].start()
        threads[i].join()
#这里通过多线程条用浏览器进行用例测试，其中IE浏览器路径有点问题
#这里就不弄了，
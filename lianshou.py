from selenium.webdriver import Remote
lists ={
    'http://127.0.0.1:4444/wd/hub': 'chrome',
    'http://127.0.0.1:4445/wd/hub':'firefox',
    'http://127.0.0.1:4455/wd/hub':'chrome'
}
for host,browser in lists.items():


    driver = Remote(command_executor=host,
                    desired_capabilities={
                        'platform':'ANY',
                        'browserName':browser,
                        'version':'',
                        'javascriptEnabled':'True'
                    })
    driver.get('http://www.baidu.com')
    driver.find_element_by_id('kw').send_keys('美女')
    driver.find_element_by_id('su').click()
    driver.close()
    #由于Firefox 和IE浏览器引擎可能出了点问题，因此运行过程中无法进行
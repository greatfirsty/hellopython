import os,time
k = 1
while k<2:
    now_time = time.strftime("%H_%M")
    if now_time == '17_49':
        print('start ')
        os.chdir(r'C:\\Users\hss\workgit\hellopython\test_project')
        os.system('python testrun.py')
        print('end')
        break
    else:
        time.sleep(10)
        print(now_time)
        #设置定时任务
        #可以通过window，Ubuntu发布任务执行

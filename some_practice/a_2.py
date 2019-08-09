from time import sleep,ctime
import multiprocessing
import threading




def super_player(file,time):
    for i in range(2):
        print('start palying {} and {}'.format(file,ctime))
        sleep(time)
list = {'爱情买卖.mp3':3,'阿凡达.mp4':4}
threads = []
files = range(len(list))
for file,time in list.items():
    t = multiprocessing.Process(target=super_player,args=(file,time))
    threads.append(t)

class myThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def run(self):
        self.func(*self.args)
list1 = {'爱情买卖.mp3':3,'阿凡达.mp4':4}
threadsd = []
filed = range(len(list1))
for file,time in list1.items():
    tt = myThread(super_player,(file,time),super_player.__name__)
    threadsd.append(tt)
if __name__ == '__main__':
    for i in files:
        threads[i].start()
        threadsd[i].start()
    for i in files:
        threads[i].join()
        threadsd[i].join()
#多线程和多进程简单使用，其中多线程使用了类方法，
#两种方法其实使用形式基本相同，就是将函数对象放入模块，执行

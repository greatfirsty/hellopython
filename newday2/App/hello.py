import time
def total_time(fun):
    def f():
        before_time=time.time()
        fun()
        current_time=time.time()
        t_time=current_time-before_time
        print(t_time)
    return f
@total_time
def add():
    time.sleep(1)
    return 3
#为函数添加装饰器，统计时间
@total_time
def sub():
    print('睡不好')
    time.sleep(2)
    print('很烦')
    return 10

if __name__=='__main__':
 sub()


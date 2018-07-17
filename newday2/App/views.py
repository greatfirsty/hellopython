import time
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page


def index(request):
    return HttpResponse('ok')

#数据库做缓存

@cache_page(20)
def get_sleep(request):
    time.sleep(5)
    print('学习')
    return HttpResponse('ok')
#再来个redis做缓存
#通过修改settings,cache配置，同
# 时启动redis-server，在同一视图函数中实现缓存运用





#前端实现富文本
def get_last(request):
    if request.method=='GET':

     return render(request,'richtext.html')
    elif request.method=='POST':
        content=request.POST.get('content')
        print(content)
        return HttpResponse('ok')

#后台站点富文本,
#后台实现富文本，需要tiny_mce,进行配置，在settings中，
# install Apps和 tinymce_defualt_config,
#配置完成之后，创建模型，进行注册即可


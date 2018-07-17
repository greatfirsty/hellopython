from django.conf.urls import url

from App import views

urlpatterns=[
    url(r'^index/',views.index,name='index'),
    url(r'getsleep/',views.get_sleep),
    url(r'^getlast/',views.get_last),
    url(r'^getlast/',views.get_last,name='getlast'),
]
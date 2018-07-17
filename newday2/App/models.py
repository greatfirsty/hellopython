from django.db import models
from tinymce.models import HTMLField
# Create your models here.
class User(models.Model):
    u_name=models.CharField(max_length=16,verbose_name='姓名')
    u_age=models.IntegerField(default=18,verbose_name='年龄')
    u_score=models.IntegerField(default=60,verbose_name='分数')

    def __str__(self):
        return self.u_name
    class Meta:
        ordering=['-u_score']

#富文本模型
class MyBook(models.Model):
    m_name=models.CharField(max_length=32,verbose_name='书名')
    m_content=HTMLField()

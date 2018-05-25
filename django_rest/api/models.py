from django.db import models

# Create your models here.

#发布会
class Event(models.Model):
    """docstring for Event"""
    '''__str__ 类实例字符串化函数'''
    name = models.CharField(max_length = 100)
    limit = models.IntegerField()
    status = models.BooleanField()
    address = models.CharField(max_length = 200)
    #修改DateTimeField返回字段默认值为 events time
    start_time = models.DateTimeField('events time')
    create_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


#嘉宾

class  Guest(models.Model):
    """docstring for  Guest"""
    #建一个外键，通过它可以获得所对应的所有信息
    event = models.ForeignKey(Event)
    realname = models.CharField(max_length = 64)
    phone = models.CharField(max_length = 16)
    email = models.EmailField()
    sign = models.BooleanField()
    create_time = models.DateTimeField(auto_now = True)

    #页面中需要展示的元属性
    class Meta:
        unique_together = ('phone','event')

    #类实例字符串化函数
    def __str__(self):
        return self.realname









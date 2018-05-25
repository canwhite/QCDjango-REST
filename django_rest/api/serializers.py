#serializers.py
from django.contrib.auth.models import User,Group
from api.models import Event,Guest
from rest_framework import serializers

#序列化 (Serialization)将对象的状态信息转换为可以存储或传输的形式的过程。
#在序列化期间，对象将其当前状态写入到临时或持久性存储区。
#以后，可以通过从存储区中读取或反序列化对象的状态，重新创建该对象。
class UserSerializer(serializers.HyperlinkedModelSerializer):
    """docstring for UserSerializer"""
    #Meta 元素可提供相关页面的元信息
    class Meta:
        model = User
        fields = ('url','username','email','groups')



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """docstring for ClassName"""
    #Meta 元素可提供相关页面的元信息
    class Meta:
        """docstring for Meta"""
        model = Group
        fields = ('url','name')

#添加发布会序列化

class EventSerializer(serializers.HyperlinkedModelSerializer):
    """docstring for EventSerializer"""
    class Meta:
        """docstring for Meta:"""
        model = Event
        fields = ('url','name','address','start_time','limit','status')


class GuestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        """docstring for Meta"""
        model = Guest
        fields = ('url','realname','phone','email','sign','event')











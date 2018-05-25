from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from api.serializers import UserSerializer,GroupSerializer,EventSerializer,GuestSerializer
from api.models import Event,Guest


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    #order_by 根据指定的列对结果集进行排序
    queryset = User.objects.all().order_by('-date_joined')
    #将写好的序列化类赋值给serializer_class,
    serializer_class = UserSerializer
    #使用queryset和serializer_class使我们能更好的控制api行为，这是我们推荐的使用方式
    #另外django_rest_framework中，所有常见的行为都被归到ViewSets中


class GroupViewSet(viewsets.ModelViewSet):
    """docstring for GroupViewSet"""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

#viewSets define the view behavior
class EventViewSet(viewsets.ModelViewSet):
    """api 端点允许事件查看和编辑"""
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class GuestViewSet(viewsets.ModelViewSet):
    """api 端点允许事件查看和编辑"""
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer







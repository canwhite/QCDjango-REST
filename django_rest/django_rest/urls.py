"""django_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
#因为我们使用的是viewset，所以我们可以使用路由器类自动生成 URL conf
from rest_framework import routers
from api import views

'''路由器提供了一种简单的方法自动确定URL配置。'''
#初始化路由器
router = routers.DefaultRouter()
#确定URL配置
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)
router.register(r'event',views.EventViewSet)
router.register(r'guest',views.GuestViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #把我们注册的东西拿出来
    url(r'^',include(router.urls)),
    #此外，我们为可浏览的api导入登陆用url
    url(r'^api-auth/',include('rest_framework.urls',namespace = 'rest_framework'))

]

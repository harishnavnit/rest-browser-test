from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^start', views.start, name='start'),
    # url(r'^start/<browser>(?P<url>)/$', views.start, name='start'),
    url(r'^geturl(?P<browser>)/$', views.geturl, name='geturl'),
    url(r'^stop(?P<browser>)/$', views.stop, name='stop'),
    url(r'^cleanup(?P<browser>)/$', views.cleanup, name='cleanup')
]

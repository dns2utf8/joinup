from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^tag/(?P<tag_name>([\w-]+))/$', views.tag_view, name='tag_view'),
    url(r'^(?P<group_name>([\w-]+))/$', views.group_view, name='group_view'),
    url(r'^(?P<group_name>([\w-]+))/(?P<event_name>(\w+))/$'
        , views.event_detail, name='event_detail'),
]
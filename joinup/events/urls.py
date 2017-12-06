from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    url(r'^create_group$', views.create_group, name='events_create_group'),
    url(r'^tag/(?P<tag_name>([\w-]+))/$', views.tag_view, name='tag_view'),
    url(r'^search/(?P<query>([\w-]+))/$', views.search, name='event_search'),
    url(r'^(?P<group_name>([\w-]+))/$', views.group_view, name='group_view'),
    url(r'^(?P<group_name>([\w-]+))/new_event', views.create_event, name='events_create_event'),
    url(r'^(?P<group_name>([\w-]+))/(?P<event_name>(\w+))/$'
        #url('<group_name>/<event_name>'
        , views.event_detail, name='event_detail'),
]
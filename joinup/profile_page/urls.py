from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.profile_self, name='profile_page_self'),
]
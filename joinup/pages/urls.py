from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^imprint$', views.make_page('Imprint'), name='page_imprint'),
    url(r'^about', views.make_page('About'), name='page_about'),
]
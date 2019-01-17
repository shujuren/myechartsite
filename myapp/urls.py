from django.conf.urls import url

from mycharts import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
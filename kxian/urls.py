from django.conf.urls import url

from kxian import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^kxian1.html', views.kxian1, name='kxian1'),
    url(r'^kxian2.html', views.kxian2, name='kxian2'),
    url(r'^kxian3.html', views.kxian3, name='kxian3'),
    url(r'^kxian4.html', views.kxian4, name='kxian4'),
    url(r'^duotu1.html', views.duotu1, name='duotu1'),
    url(r'^duotu2.html', views.duotu2, name='duotu2'),
    url(r'^duotu3.html', views.duotu3, name='duotu3'),
    url(r'^duotu4.html', views.duotu4, name='duotu4'),
]
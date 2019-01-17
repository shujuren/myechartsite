from django.conf.urls import include, url
from django.contrib import admin

from mycharts import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'mycharts/', include('mycharts.urls')),
    url(r'kxian/', include('kxian.urls')),
]
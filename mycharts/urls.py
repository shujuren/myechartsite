from django.conf.urls import url

from mycharts import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^mybar1.html', views.mybar1, name='mybar1'),
    url(r'^mybar2.html', views.mybar2, name='mybar2'),
    url(r'^mybar3.html', views.mybar3, name='mybar3'),
    url(r'^boxplot1.html', views.boxplot1, name='boxplot1'),
    url(r'^Scatter1.html', views.Scatter1, name='Scatter1'),
    url(r'^barpandas.html', views.barpandas, name='barpandas'),
    url(r'^barpandas1.html', views.barpandas1, name='barpandas1'),
    url(r'^barpandas2.html', views.barpandas2, name='barpandas2'),
    url(r'^boxplotpandas.html', views.boxplotpandas, name='boxplotpandas'),
    url(r'^boxplotpandas1.html', views.boxplotpandas1, name='boxplotpandas1'),
    url(r'^Scatter2.html', views.Scatter2, name='Scatter2'),
    url(r'^threeD1.html', views.threeD1, name='threeD1'),
    url(r'^line3d.html', views.line3d, name='line3d'),
]
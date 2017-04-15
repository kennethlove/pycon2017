from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^category/(?P<category>[-\w]+)/$', views.ByCategory.as_view(), name='category'),
    url(r'^view/(?P<slug>[-\w]+)/$', views.Detail.as_view(), name='detail'),
    url(r'^$', views.AllProducts.as_view(), name='list'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^view/(?P<slug>[-\w]+)/$', views.Detail.as_view(), name='detail'),
    url(r'^$', views.AllProducts.as_view(), name='list'),
]

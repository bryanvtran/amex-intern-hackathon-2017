from django.conf.urls import url
from dfirstapp import views

urlpatterns = [
    url(r'^$', views.showhome, name='index'),
]

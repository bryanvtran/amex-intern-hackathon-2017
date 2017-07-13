from django.conf.urls import url
from dfirstapp import views

urlpatterns = [
    url(r'^$', views.signup, name='signup'),
    url(r'^studentprof/$', views.studentprof, name='studentprof'),
    url(r'^teamprof/$', views.teamprof, name='teamprof'),
    url(r'^match/$', views.match, name='match'),
    url(r'^contact/$', views.contact, name='contact'),
]

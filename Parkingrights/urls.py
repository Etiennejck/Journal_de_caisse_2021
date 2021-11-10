from django.conf.urls import url
from django.urls import path
from Parkingrights import views

urlpatterns = [
    path('', views.parkingrights, name='parkingrights'),
    #url(r'^logging/$', views.logging, name='logging')

]
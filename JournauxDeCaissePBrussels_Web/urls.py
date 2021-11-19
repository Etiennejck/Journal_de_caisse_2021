from django.conf.urls import url
from JournauxDeCaissePBrussels_Web import views
from Journal_de_caisse_2021 import views as jcViews

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    url(r'^log_out/$', views.log_out, name='log_out'),
    #url(r'^logging/$', views.logging, name='logging')

]
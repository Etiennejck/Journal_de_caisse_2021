from django.conf.urls import url
from JournauxDeCaissePBrussels_Web import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page.html'),
    url(r'^upload_file/$', views.upload_file, name='upload_file'),
    #url(r'^logging/$', views.logging, name='logging')

]
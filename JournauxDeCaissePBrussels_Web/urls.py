from django.conf.urls import url
from JournauxDeCaissePBrussels_Web import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),

]
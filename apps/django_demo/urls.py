from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^', views.index, name='index'),
    url(r'^logOut', views.logOut, name='logOut'),
    url(r'^poke/', views.addPoke, name='pokeMe'),
]

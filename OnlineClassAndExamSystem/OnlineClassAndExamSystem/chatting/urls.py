from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
urlpatterns= [ 
    path('', views.home, name ='home'),
    path('<str:room>/',views.room, name ='room'),
    path('checkView', views.checkView, name ='checkView')

]
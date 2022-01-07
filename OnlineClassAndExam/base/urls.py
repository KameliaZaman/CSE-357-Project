from django.urls import path
from . import views

urlpatterns= [

    path('',views.homePage,name="home"),

    path('topics/', views.topicsPage, name="topics"),

    path('room/<str:pk>/', views.room, name="room"),

    path('create-room/', views.createRoomSingleton, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoomSingleton, name="update-room"),
    path('delete-room/<str:pk>/', views.deleteRoomSingleton, name="delete-room"),
    path('delete-message/<str:pk>/', views.deleteMessageSingleton, name="delete-message"),

    path('activity/', views.activityPageSingleton, name="activity"),
]
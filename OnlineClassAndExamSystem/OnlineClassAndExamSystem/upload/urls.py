from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.home, name='home'),
    path('show/',views.showQuestionAndSolutionList,name='show'),
    path('uploadsolution/',views.uploadQuestionAndSolution,name='uploadQuesAndSolve')

]

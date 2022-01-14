from django.urls import path
from . import views 

urlpatterns = [
  path('', views.uploadAssignments, name='uploadAssignments'),
  path('showassignments/', views.showAssignments, name='showAssignments'),
  path('pendingassignments/', views.pendingAssignments, name='pendingAssignments'),
  path('submissionpage/', views.submissionPage, name='submissionpage'),
  path('viewsubmission/', views.viewSubmission, name='viewSubmission') 



]


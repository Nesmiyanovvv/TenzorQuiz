from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/teams/', views.TeamsListAPIView.as_view()),
    path('api/v1/teams/<int:pk>/', views.TeamAPIView.as_view()),
    path('api/v1/teams/<int:pk>/join/', views.join_team),
    path('api/v1/teams/<int:pk>/leave/', views.leave_team),
    path('api/v1/teams/myteams/', views.my_teams),
]

from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('', views.StaffDashboardView.as_view(), name='home'),
    path('schedule/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='schedule'),
    path('participants/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='participants'),
    path('tasks/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='tasks'),
    path('care-notes/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='care_notes'),
    path('medications/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='medications'),
    path('incidents/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='incidents'),
    path('documents/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='documents'),
    path('messages/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='messages'),
    path('leave/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='leave'),
    path('profile/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='profile'),
    path('settings/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='settings'),
]

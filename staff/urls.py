from django.urls import path
from . import views
from dashboard.views import StaffMyDashboardView, StaffParticipantListView, StaffParticipantDetailView

app_name = 'staff'

urlpatterns = [
    path('', views.StaffDashboardView.as_view(), name='home'),
    path('schedule/', StaffMyDashboardView.as_view(), name='schedule'),
    path('participants/', StaffParticipantListView.as_view(), name='participants'),
    path('participants/<int:pk>/', StaffParticipantDetailView.as_view(), name='participant_profile'),
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

from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Main Dashboard
    path('', views.DashboardHomeView.as_view(), name='home'),
    
    # Placeholder routes for sidebar links
    path('participants/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='participants'),
    path('staff/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='staff'),
    path('coordinators/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='coordinators'),
    path('referrals/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='referrals'),
    path('appointments/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='appointments'),
    path('roster/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='roster'),
    path('agreements/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='agreements'),
    path('plans/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='plans'),
    path('incidents/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='incidents'),
    path('documents/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='documents'),
    path('billing/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='billing'),
    path('claims/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='claims'),
    path('reports/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='reports'),
    path('blogs/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='blogs'),
    path('settings/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='settings'),
]

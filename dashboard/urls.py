from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    # Main Dashboard
    path('', views.DashboardHomeView.as_view(), name='home'),
    
    # Placeholder routes for sidebar links
    # Participant Management
    path('participants/', views.ParticipantListView.as_view(), name='participants'),
    path('participants/profile/', views.ParticipantProfileView.as_view(), name='participant_profile'),
    path('participants/<int:pk>/', views.ParticipantProfileView.as_view(), name='participant_profile_detail'),
    path('staff/', views.StaffListView.as_view(), name='staff'),
    path('staff/profile/', views.StaffProfileView.as_view(), name='staff_profile'),
    path('staff/<int:pk>/', views.StaffProfileView.as_view(), name='staff_profile_detail'),
    path('staff/my-dashboard/', views.StaffMyDashboardView.as_view(), name='staff_my_dashboard'),
    path('staff/check-in/<int:pk>/', views.VisitCheckInView.as_view(), name='visit_check_in'),
    path('staff/check-out/<int:pk>/', views.VisitCheckOutView.as_view(), name='visit_check_out'),
    path('reviews/', views.AdminReviewVisitsView.as_view(), name='admin_review_visits'),
    path('coordinators/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='coordinators'),
    path('referrals/', views.ReferralListView.as_view(), name='referrals'),
    path('referrals/new/', views.ReferralCreateView.as_view(), name='referral_new'),
    path('referrals/<int:pk>/', views.ReferralDetailView.as_view(), name='referral_profile_detail'),
    path('appointments/', views.AppointmentListView.as_view(), name='appointments'),
    path('appointments/<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    path('roster/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='roster'),
    path('agreements/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='agreements'),
    path('plans/', views.SupportPlanListView.as_view(), name='plans'),
    path('plans/<int:pk>/', views.SupportPlanDetailView.as_view(), name='plan_detail'),
    path('incidents/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='incidents'),
    path('documents/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='documents'),
    path('billing/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='billing'),
    path('claims/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='claims'),
    path('reports/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='reports'),
    path('blogs/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='blogs'),
    path('settings/', views.PlaceholderView.as_view(template_name="dashboard/placeholder.html"), name='settings'),
]

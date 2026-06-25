from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.DashboardView.as_view(), name='index'),
    path('login/', views.PortalLoginView.as_view(), name='login'),
    path('logout/', views.PortalLogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    
    # Participant Management
    path('participants/', views.ParticipantListView.as_view(), name='participant_list'),
    path('participants/<int:pk>/', views.ParticipantDetailView.as_view(), name='participant_detail'),
    
    # Referral Management
    path('referrals/', views.ReferralListView.as_view(), name='referral_list'),
    path('referrals/<int:pk>/', views.ReferralDetailView.as_view(), name='referral_detail'),
    
    # Other placeholder routes
    path('support-plans/', views.SupportPlanListView.as_view(), name='support_plans'),
    path('case-notes/', views.CaseNoteListView.as_view(), name='case_notes'),
    path('documents/', views.DocumentListView.as_view(), name='documents'),
    path('leave/', views.LeaveRequestListView.as_view(), name='leave_requests'),
    path('announcements/', views.AnnouncementListView.as_view(), name='announcements'),
    path('reports/', views.ReportView.as_view(), name='reports'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]

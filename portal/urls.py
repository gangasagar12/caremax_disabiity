from django.urls import path
from . import views

app_name = 'portal'

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('login/', views.portal_login, name='login'),
    path('logout/', views.portal_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Participant Management
    path('participants/', views.participant_list, name='participant_list'),
    path('participants/<int:pk>/', views.participant_detail, name='participant_detail'),
    
    # Referral Management
    path('referrals/', views.referral_list, name='referral_list'),
    path('referrals/<int:pk>/', views.referral_detail, name='referral_detail'),
    
    # Other placeholder routes
    path('support-plans/', views.support_plans, name='support_plans'),
    path('case-notes/', views.case_notes, name='case_notes'),
    path('documents/', views.documents, name='documents'),
    path('leave/', views.leave_requests, name='leave_requests'),
    path('announcements/', views.announcements, name='announcements'),
    path('reports/', views.reports, name='reports'),
    path('profile/', views.profile, name='profile'),
]

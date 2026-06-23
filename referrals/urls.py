from django.urls import path
from . import views

app_name = 'referrals'

urlpatterns = [
    path('', views.ReferralCreateView.as_view(), name='referral_create'),
    path('success/', views.ReferralSuccessView.as_view(), name='referral_success'),
]

from django.urls import path
from django.views.generic import TemplateView

app_name = 'services'

urlpatterns = [
    path('', TemplateView.as_view(template_name='services/service_list.html'), name='service_list'),
    path('assistance-with-daily-life/', TemplateView.as_view(template_name='services/assistance_with_daily_life.html')),
    path('household-tasks/', TemplateView.as_view(template_name='services/household_tasks.html')),
    path('travel-and-transport/', TemplateView.as_view(template_name='services/travel_and_transport.html')),
    path('social-and-community-participation/', TemplateView.as_view(template_name='services/social_and_community_participation.html')),
    path('shared-living-and-sil/', TemplateView.as_view(template_name='services/shared_living_and_sil.html')),
    path('group-and-centre-activities/', TemplateView.as_view(template_name='services/group_and_centre_activities.html')),
    path('daily-living-skills/', TemplateView.as_view(template_name='services/daily_living_skills.html')),
    path('employment-and-education-support/', TemplateView.as_view(template_name='services/employment_and_education_support.html')),
]

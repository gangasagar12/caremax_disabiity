from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class DashboardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboard'


class CustomAdminConfig(AdminConfig):
    default_site = 'dashboard.admin.CustomAdminSite'

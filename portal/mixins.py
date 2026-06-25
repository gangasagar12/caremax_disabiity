from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from .models import ActivityLog

class StaffRequiredMixin(UserPassesTestMixin):
    """
    Verify that the current user is authenticated and belongs to the 'Staff Group'.
    """
    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.groups.filter(name='Staff Group').exists() or 
            self.request.user.is_superuser
        )

    def handle_no_permission(self):
        # Redirect to login or a 403 page
        if not self.request.user.is_authenticated:
            return redirect('portal:login')
        return super().handle_no_permission()

class ActivityLogMixin:
    """
    Mixin to automatically log activity for Create/Update/Delete views.
    Should be used with form_valid method.
    """
    def log_activity(self, action, details=""):
        if self.request.user.is_authenticated:
            ip = self.request.META.get('REMOTE_ADDR')
            ActivityLog.objects.create(
                user=self.request.user,
                action=action,
                details=details,
                ip_address=ip
            )

    def form_valid(self, form):
        response = super().form_valid(form)
        action = f"Created/Updated {self.model.__name__ if hasattr(self, 'model') and self.model else 'Record'}"
        details = str(self.object) if hasattr(self, 'object') else ""
        self.log_activity(action, details)
        return response

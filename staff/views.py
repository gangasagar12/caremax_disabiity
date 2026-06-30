from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class StaffDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "staff/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Placeholder stats for the UI
        context['stats'] = {
            'today_appointments': 4,
            'active_participants': 12,
            'completed_visits': 1,
            'pending_notes': 2,
            'incident_reports': 0,
            'upcoming_tasks': 5,
        }
        return context

class PlaceholderView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/placeholder.html"

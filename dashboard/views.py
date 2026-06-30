from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Placeholder stats for the UI
        context['stats'] = {
            'total_participants': 142,
            'participants_trend': '+12%',
            'active_workers': 38,
            'workers_trend': '+5%',
            'today_visits': 86,
            'visits_trend': '+18%',
            'pending_referrals': 14,
            'referrals_trend': '-2%',
            'upcoming_appointments': 32,
            'revenue_month': '$124,500',
            'revenue_trend': '+24%',
            'claims_pending': '$18,200',
            'incident_reports': 2,
            'incident_trend': '-50%'
        }
        return context

class PlaceholderView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/placeholder.html"

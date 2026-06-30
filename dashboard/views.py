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

class ParticipantListView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/participants/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Mock data for list view stats
        context['stats'] = {
            'total': 156,
            'active': 142,
            'pending': 12,
            'inactive': 2
        }
        
        # Dynamic filter options
        context['filter_statuses'] = ['Active', 'Pending', 'Inactive']
        context['filter_staff'] = ['Michael Chang', 'Sarah Connor', 'John Doe']
        context['filter_services'] = ['Core Support', 'Capacity Building', 'Capital']
        
        # Dynamic participant list
        context['participants'] = [
            {
                'pk': 10045,
                'id_str': 'PT-10045',
                'name': 'Sarah Jenkins',
                'ndis': '430 998 123',
                'age': 34,
                'gender': 'Female',
                'phone': '0412 345 678',
                'staff': 'Michael Chang',
                'staff_initials': 'MC',
                'staff_color': 'success',
                'support_level': 'High',
                'status': 'Active',
                'status_class': 'status-active',
                'next_appt': 'Oct 15, 2024',
                'initials': 'SJ',
                'has_avatar': False
            },
            {
                'pk': 10046,
                'id_str': 'PT-10046',
                'name': 'David Miller',
                'ndis': '430 887 654',
                'age': 45,
                'gender': 'Male',
                'phone': '0412 987 654',
                'staff': 'Sarah Connor',
                'staff_initials': 'SC',
                'staff_color': 'warning',
                'support_level': 'Standard',
                'status': 'Active',
                'status_class': 'status-active',
                'next_appt': 'Oct 18, 2024',
                'avatar_url': 'https://i.pravatar.cc/150?u=a042581f4e29026704d',
                'has_avatar': True
            },
            {
                'pk': 10047,
                'id_str': 'PT-10047',
                'name': 'Emily Rose',
                'ndis': '430 776 543',
                'age': 28,
                'gender': 'Female',
                'phone': '0423 456 789',
                'staff': None,
                'support_level': 'Complex',
                'status': 'Pending',
                'status_class': 'status-pending',
                'next_appt': '-',
                'initials': 'ER',
                'has_avatar': False
            }
        ]
        
        return context

class ParticipantProfileView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/participants/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Mock participant data
        context['participant'] = {
            'id': kwargs.get('pk', 'PT-10045'),
            'name': 'Sarah Jenkins',
            'status': 'Active',
            'ndis_number': '430 998 123',
            'assigned_staff': 'Michael Chang',
            'emergency_contact': 'David Jenkins (Husband)',
            'phone': '0412 345 678',
            'email': 'sarah.j@example.com'
        }
        return context

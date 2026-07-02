from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.models import Appointment, SupportPlan, Participant, VisitRecord
from django.utils import timezone

class StaffDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "staff/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            worker = self.request.user.support_worker_profile
            today = timezone.now().date()
            
            # Today's appointments
            today_appointments = Appointment.objects.filter(staff=worker, date=today).order_by('start_time')
            
            # Assigned Participants via SupportPlans
            assigned_plans = SupportPlan.objects.filter(assigned_staff=worker).select_related('participant')
            assigned_participants = []
            for plan in assigned_plans:
                p = plan.participant
                # Find next appointment for this participant
                p.next_appt = Appointment.objects.filter(participant=p, staff=worker, date__gte=today).order_by('date', 'start_time').first()
                p.support_plan = plan
                assigned_participants.append(p)
                
            # Completed Visits Today
            completed_today = today_appointments.filter(status='Completed')
            
            # Pending Notes (Completed today but no VisitRecord or empty care_notes)
            # Find appointments completed today that don't have a visit record or have one with no notes
            pending_notes_count = 0
            for appt in completed_today:
                try:
                    vr = appt.visit_record
                    if not vr.care_notes:
                        pending_notes_count += 1
                except VisitRecord.DoesNotExist:
                    pending_notes_count += 1
            
            context['today'] = today
            context['today_appointments'] = today_appointments
            context['assigned_participants'] = assigned_participants
            
            context['stats'] = {
                'today_appointments': today_appointments.count(),
                'active_participants': len(assigned_participants),
                'completed_visits': completed_today.count(),
                'pending_notes': pending_notes_count,
            }
            
        except Exception as e:
            # Fallback if the user is not a staff member
            context['today'] = timezone.now().date()
            context['today_appointments'] = []
            context['assigned_participants'] = []
            context['stats'] = {
                'today_appointments': 0,
                'active_participants': 0,
                'completed_visits': 0,
                'pending_notes': 0,
            }
            
        return context

class PlaceholderView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/placeholder.html"

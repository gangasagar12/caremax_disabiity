from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from django.views import View
from .models import Participant, SupportWorker, Appointment, VisitRecord, VisitDocument, SupportPlan

class DashboardHomeView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        
        total_participants = Participant.objects.count()
        active_workers = SupportWorker.objects.filter(status='Active').count()
        today_visits = Appointment.objects.filter(date=now.date()).count()
        
        context['stats'] = {
            'total_participants': total_participants,
            'participants_trend': '+0%',
            'active_workers': active_workers,
            'workers_trend': '+0%',
            'today_visits': today_visits,
            'visits_trend': '+0%',
            'pending_referrals': 0,
            'referrals_trend': '0%',
            'upcoming_appointments': Appointment.objects.filter(date__gte=now.date()).count(),
            'revenue_month': '$0',
            'revenue_trend': '0%',
            'claims_pending': '$0',
            'incident_reports': 0,
            'incident_trend': '0%'
        }
        return context

class PlaceholderView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/placeholder.html"

class ParticipantListView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/participants/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        total = Participant.objects.count()
        active = Participant.objects.filter(status='Active').count()
        pending = Participant.objects.filter(status='Pending').count()
        inactive = Participant.objects.filter(status='Inactive').count()
        
        context['stats'] = {
            'total': total,
            'active': active,
            'pending': pending,
            'inactive': inactive
        }
        
        context['filter_statuses'] = ['Active', 'Pending', 'Inactive']
        context['filter_staff'] = [s.user.get_full_name() for s in SupportWorker.objects.all()]
        context['filter_services'] = ['Core Support', 'Capacity Building', 'Capital']
        
        participants_data = []
        for p in Participant.objects.all():
            first_initial = p.first_name[0] if p.first_name else ''
            last_initial = p.last_name[0] if p.last_name else ''
            
            appt = p.appointments.first()
            staff_name = appt.staff.user.get_full_name() if appt else None
            staff_initials = (appt.staff.user.first_name[0] + appt.staff.user.last_name[0]) if (appt and appt.staff.user.first_name) else 'N/A'
            
            status_class = 'status-active'
            if p.status == 'Pending':
                status_class = 'status-pending'
            elif p.status == 'Inactive':
                status_class = 'status-inactive'
                
            participants_data.append({
                'pk': p.pk,
                'id_str': p.ndis_number or f'PT-{10000 + p.pk}',
                'name': f"{p.first_name} {p.last_name}",
                'ndis': p.ndis_number,
                'age': 30,
                'gender': 'Not specified',
                'phone': p.phone,
                'staff': staff_name,
                'staff_initials': staff_initials,
                'staff_color': 'success' if staff_name else 'secondary',
                'support_level': 'Standard',
                'status': p.status,
                'status_class': status_class,
                'next_appt': str(appt.date) if appt else '-',
                'initials': f"{first_initial}{last_initial}",
                'has_avatar': False
            })
            
        context['participants'] = participants_data
        return context

class ParticipantProfileView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/participants/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        try:
            p = Participant.objects.get(pk=pk)
            appt = p.appointments.first()
            context['participant'] = {
                'id': p.ndis_number or f'PT-{10000 + p.pk}',
                'name': f"{p.first_name} {p.last_name}",
                'status': p.status,
                'ndis_number': p.ndis_number,
                'assigned_staff': appt.staff.user.get_full_name() if appt else 'None',
                'emergency_contact': 'Not specified',
                'phone': p.phone,
                'email': p.email
            }
        except Participant.DoesNotExist:
            context['participant'] = {}
        return context

class StaffListView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/staff/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        total = SupportWorker.objects.count()
        active = SupportWorker.objects.filter(status='Active').count()
        inactive = SupportWorker.objects.filter(status='Inactive').count()
        on_leave = SupportWorker.objects.filter(status='On Leave').count()
        
        context['stats'] = {
            'total': total,
            'active': active,
            'inactive': inactive,
            'on_leave': on_leave,
            'working_today': Appointment.objects.filter(date=timezone.now().date()).values('staff').distinct().count(),
            'cert_expiring': 0
        }
        
        context['filter_departments'] = ['Nursing', 'Allied Health', 'Support Services']
        context['filter_positions'] = ['Support Worker', 'Registered Nurse', 'Coordinator']
        context['filter_employment'] = ['Full-Time', 'Part-Time', 'Casual']
        
        staff_data = []
        for s in SupportWorker.objects.all():
            user = s.user
            first_initial = user.first_name[0] if user.first_name else ''
            last_initial = user.last_name[0] if user.last_name else ''
            
            status_class = 'status-active'
            color = 'success'
            if s.status == 'On Leave':
                status_class = 'status-pending'
                color = 'warning'
            elif s.status == 'Inactive':
                status_class = 'status-inactive'
                color = 'danger'
                
            today_appts = Appointment.objects.filter(staff=s, date=timezone.now().date()).count()
            assigned_participants = Appointment.objects.filter(staff=s).values('participant').distinct().count()
            
            staff_data.append({
                'pk': s.pk,
                'employee_id': s.employee_id,
                'name': user.get_full_name(),
                'position': 'Support Worker',
                'phone': s.phone,
                'email': user.email,
                'assigned_participants': assigned_participants,
                'today_appointments': today_appts,
                'status': s.status,
                'status_class': status_class,
                'last_login': user.last_login.strftime('%b %d, %Y') if user.last_login else 'Never',
                'initials': f"{first_initial}{last_initial}",
                'color': color,
                'has_avatar': False
            })
            
        context['staff_list'] = staff_data
        return context

class StaffProfileView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/staff/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        try:
            s = SupportWorker.objects.get(pk=pk)
            user = s.user
            context['staff'] = {
                'pk': s.pk,
                'employee_id': s.employee_id,
                'name': user.get_full_name(),
                'position': 'Support Worker',
                'status': s.status,
                'department': 'Support Services',
                'phone': s.phone,
                'email': user.email,
                'manager': 'Admin',
                'employment_type': 'Full-Time',
                'joining_date': user.date_joined.strftime('%d %b %Y') if user.date_joined else 'Unknown',
            }
        except SupportWorker.DoesNotExist:
            context['staff'] = {}
        return context

class StaffMyDashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/staff_my_dashboard.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            worker = self.request.user.support_worker_profile
            today = timezone.now().date()
            appointments = Appointment.objects.filter(staff=worker, date=today)
            context['appointments'] = appointments
            context['worker'] = worker
        except:
            context['appointments'] = []
            context['worker'] = None
        return context

class VisitCheckInView(LoginRequiredMixin, View):
    def post(self, request, pk):
        appt = get_object_or_404(Appointment, pk=pk)
        visit, created = VisitRecord.objects.get_or_create(appointment=appt)
        if not visit.check_in_time:
            visit.check_in_time = timezone.now()
            visit.save()
            appt.status = 'In Progress'
            appt.save()
        return redirect('dashboard:staff_my_dashboard')

class VisitCheckOutView(LoginRequiredMixin, View):
    def post(self, request, pk):
        appt = get_object_or_404(Appointment, pk=pk)
        visit = get_object_or_404(VisitRecord, appointment=appt)
        
        care_notes = request.POST.get('care_notes', '')
        
        visit.check_out_time = timezone.now()
        visit.care_notes = care_notes
        visit.save()
        
        appt.status = 'Completed'
        appt.save()
        
        if 'document' in request.FILES:
            VisitDocument.objects.create(visit=visit, file_upload=request.FILES['document'])
            
        return redirect('dashboard:staff_my_dashboard')

class AdminReviewVisitsView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/admin_review_visits.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        completed_visits = VisitRecord.objects.filter(appointment__status='Completed').order_by('-check_out_time')
        context['visits'] = completed_visits
        return context

class AppointmentListView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/appointments/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        today = now.date()
        
        appointments = Appointment.objects.all().order_by('date', 'start_time')
        
        context['stats'] = {
            'today': appointments.filter(date=today).count(),
            'completed_today': appointments.filter(date=today, status='Completed').count(),
            'upcoming': appointments.filter(date__gte=today, status__in=['Scheduled', 'In Progress']).count(),
            'cancelled': appointments.filter(status='Cancelled').count(),
            'staff_working': appointments.filter(date=today).values('staff').distinct().count(),
        }
        
        context['appointments'] = appointments
        context['participants'] = Participant.objects.filter(status='Active')
        context['staff_members'] = SupportWorker.objects.filter(status='Active')
        return context

class AppointmentDetailView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/appointments/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        appt = get_object_or_404(Appointment, pk=pk)
        context['appointment'] = appt
        
        try:
            context['visit'] = appt.visit_record
        except:
            context['visit'] = None
            
        return context

class SupportPlanListView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/plans/list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        plans = SupportPlan.objects.all().order_by('-updated_at')
        
        context['stats'] = {
            'total': plans.count(),
            'active': plans.filter(status='Active').count(),
            'review_due': plans.filter(status='Review Due').count(),
            'expired': plans.filter(status='Expired').count(),
        }
        
        context['plans'] = plans
        context['participants'] = Participant.objects.filter(status='Active')
        context['staff_members'] = SupportWorker.objects.filter(status='Active')
        return context

class SupportPlanDetailView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/plans/profile.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get('pk')
        plan = get_object_or_404(SupportPlan, pk=pk)
        context['plan'] = plan
        return context

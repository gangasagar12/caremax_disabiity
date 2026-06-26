from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy

from .models import Participant, SupportPlan, CaseNote, Document, LeaveRequest, Announcement, Notification
from referrals.models import Referral
from .mixins import StaffRequiredMixin, ActivityLogMixin

class PortalLoginView(LoginView):
    template_name = 'portal/login.html'
    
    def get_success_url(self):
        return reverse_lazy('portal:dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.request.session['portal_logged_in'] = True
        return response

class PortalLogoutView(LogoutView):
    next_page = reverse_lazy('portal:login')
    http_method_names = ['get', 'post', 'options']

    def get(self, request, *args, **kwargs):
        from django.contrib.auth import logout
        logout(request)
        return redirect(self.next_page)

class DashboardView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        is_admin = user.is_superuser or user.has_perm('auth.view_user')
        context['is_admin'] = is_admin

        if is_admin:
            participants = Participant.objects.all().prefetch_related('assigned_staff')
            referrals = Referral.objects.all().select_related('assigned_staff').prefetch_related('services_required')
        else:
            from guardian.shortcuts import get_objects_for_user
            participants = get_objects_for_user(user, 'portal.view_participant').prefetch_related('assigned_staff')
            referrals = get_objects_for_user(user, 'referrals.view_referral').select_related('assigned_staff').prefetch_related('services_required')
        
        context['total_participants'] = participants.count()
        context['active_participants'] = participants.filter(status='Active').count()
        
        context['new_referrals'] = referrals.filter(status='New').count()
        context['pending_referrals'] = referrals.filter(status__in=['Contacted', 'Assessment Scheduled', 'In Progress']).count()
        
        context['recent_referrals'] = referrals.order_by('-created_at')[:5]
        return context

class ParticipantListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    template_name = 'portal/participants/list.html'
    context_object_name = 'participants'
    paginate_by = 20
    
    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get('q', '')
        status_filter = self.request.GET.get('status', '')
        
        is_admin = user.is_superuser or user.has_perm('auth.view_user')
        if is_admin:
            participants = Participant.objects.all().order_by('-created_at').prefetch_related('assigned_staff')
        else:
            from guardian.shortcuts import get_objects_for_user
            participants = get_objects_for_user(user, 'portal.view_participant').order_by('-created_at').prefetch_related('assigned_staff')
        
        if query:
            participants = participants.filter(first_name__icontains=query) | participants.filter(last_name__icontains=query) | participants.filter(ndis_number__icontains=query)
            
        if status_filter:
            participants = participants.filter(status=status_filter)
            
        return participants
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['status_filter'] = self.request.GET.get('status', '')
        return context

class ParticipantDetailView(LoginRequiredMixin, StaffRequiredMixin, DetailView):
    template_name = 'portal/participants/detail.html'
    context_object_name = 'participant'
    
    def get_queryset(self):
        user = self.request.user
        is_admin = user.is_superuser or user.has_perm('auth.view_user')
        if is_admin:
            return Participant.objects.all()
        from guardian.shortcuts import get_objects_for_user
        return get_objects_for_user(user, 'portal.view_participant')

class ReferralListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    template_name = 'portal/referrals/list.html'
    context_object_name = 'referrals'
    paginate_by = 20
    
    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get('q', '')
        status_filter = self.request.GET.get('status', '')
        
        is_admin = user.is_superuser or user.has_perm('auth.view_user')
        if is_admin:
            referrals = Referral.objects.all().order_by('-created_at').select_related('assigned_staff').prefetch_related('services_required')
        else:
            from guardian.shortcuts import get_objects_for_user
            referrals = get_objects_for_user(user, 'referrals.view_referral').order_by('-created_at').select_related('assigned_staff').prefetch_related('services_required')
        
        if query:
            referrals = referrals.filter(first_name__icontains=query) | referrals.filter(last_name__icontains=query)
            
        if status_filter:
            referrals = referrals.filter(status=status_filter)
            
        return referrals
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        context['status_filter'] = self.request.GET.get('status', '')
        return context

class ReferralDetailView(LoginRequiredMixin, StaffRequiredMixin, DetailView):
    template_name = 'portal/referrals/detail.html'
    context_object_name = 'referral'
    
    def get_queryset(self):
        user = self.request.user
        is_admin = user.is_superuser or user.has_perm('auth.view_user')
        if is_admin:
            return Referral.objects.all()
        from guardian.shortcuts import get_objects_for_user
        return get_objects_for_user(user, 'referrals.view_referral')

class SupportPlanListView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Support Plans'
        return context

class CaseNoteListView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Case Notes'
        return context

class DocumentListView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Documents'
        return context

class LeaveRequestListView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Leave Requests'
        return context

class AnnouncementListView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Announcements'
        return context

class ReportView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reports'
        return context

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Profile'
        return context

class EmployeeListView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Employees'
        return context

class WebsiteMessageListView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Website Messages'
        return context

class UserManagementView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'User Management'
        return context

class SettingsView(LoginRequiredMixin, StaffRequiredMixin, TemplateView):
    template_name = 'portal/placeholder.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Settings'
        return context

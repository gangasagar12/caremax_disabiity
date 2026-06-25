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
        
        # Staff specific statistics
        assigned_participants = user.assigned_participants.all()
        assigned_referrals = Referral.objects.filter(assigned_staff=user)
        
        context['total_participants'] = assigned_participants.count()
        context['active_participants'] = assigned_participants.filter(status='Active').count()
        
        context['new_referrals'] = assigned_referrals.filter(status='New').count()
        context['pending_referrals'] = assigned_referrals.filter(status__in=['Contacted', 'Assessment Scheduled', 'In Progress']).count()
        
        context['recent_referrals'] = assigned_referrals.order_by('-created_at')[:5]
        return context

class ParticipantListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    template_name = 'portal/participants/list.html'
    context_object_name = 'participants'
    
    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get('q', '')
        status_filter = self.request.GET.get('status', '')
        
        participants = user.assigned_participants.all().order_by('-created_at')
        
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
        return self.request.user.assigned_participants.all()

class ReferralListView(LoginRequiredMixin, StaffRequiredMixin, ListView):
    template_name = 'portal/referrals/list.html'
    context_object_name = 'referrals'
    
    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get('q', '')
        status_filter = self.request.GET.get('status', '')
        
        referrals = Referral.objects.filter(assigned_staff=user).order_by('-created_at')
        
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
        return Referral.objects.filter(assigned_staff=self.request.user)

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

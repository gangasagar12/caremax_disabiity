from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from .models import Referral, ReferralService
from .forms import ReferralForm

class ReferralCreateView(CreateView):
    model = Referral
    form_class = ReferralForm
    template_name = 'referrals/referral_form.html'
    success_url = reverse_lazy('referrals:referral_success')

    def form_valid(self, form):
        # Save the referral first
        response = super().form_valid(form)
        
        # Save selected services required
        services_required = form.cleaned_data.get('services_required', [])
        for service_name in services_required:
            ReferralService.objects.create(referral=self.object, service_name=service_name)
            
        return response

class ReferralSuccessView(TemplateView):
    template_name = 'referrals/referral_success.html'

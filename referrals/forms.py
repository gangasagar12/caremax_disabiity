from django import forms
from .models import Referral

class ReferralForm(forms.ModelForm):
    SERVICES_CHOICES = (
        ('Daily Personal Activities', 'Daily Personal Activities'),
        ('Household Tasks', 'Household Tasks'),
        ('Community Participation', 'Community Participation'),
        ('Travel & Transport', 'Travel & Transport'),
        ('Group & Centre Activities', 'Group & Centre Activities'),
        ('Shared Living & SIL', 'Shared Living & SIL'),
        ('Daily Living & Life Skills', 'Daily Living & Life Skills'),
        ('Employment & Education', 'Employment & Education'),
    )
    
    services_required = forms.MultipleChoiceField(
        choices=SERVICES_CHOICES, 
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Support Services Required"
    )

    class Meta:
        model = Referral
        fields = [
            'first_name', 'last_name', 'date_of_birth', 'gender', 'phone', 'email', 'address', 'ndis_number', 'plan_management',
            'support_goals', 'additional_notes',
            'referrer_name', 'relationship', 'referrer_phone', 'referrer_email'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Referral(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Non-binary', 'Non-binary'),
        ('Prefer not to say', 'Prefer not to say'),
    )
    
    PLAN_MANAGEMENT_CHOICES = (
        ('NDIA Agency Managed', 'NDIA Agency Managed'),
        ('Self Managed', 'Self Managed'),
        ('Plan Managed', 'Plan Managed'),
        ('Not Yet Approved', 'Not Yet Approved'),
        ('Not Sure', 'Not Sure'),
    )

    RELATIONSHIP_CHOICES = (
        ('Self', 'Self'),
        ('Family Member', 'Family Member'),
        ('Support Coordinator', 'Support Coordinator'),
        ('Healthcare Provider', 'Healthcare Provider'),
        ('Other', 'Other'),
    )

    STATUS_CHOICES = (
        ('New', 'New'),
        ('Contacted', 'Contacted'),
        ('Assessment Scheduled', 'Assessment Scheduled'),
        ('In Progress', 'In Progress'),
        ('Approved', 'Approved'),
        ('Closed', 'Closed'),
    )

    # Meta
    referral_id = models.CharField(max_length=20, unique=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='New')
    assigned_admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_referrals_admin')
    
    # Referral Information
    referral_date = models.DateField(default=timezone.now)
    referral_source = models.CharField(max_length=255, blank=True)
    referral_type = models.CharField(max_length=50, blank=True) # E.g., Hospital, Doctor
    
    # Participant Details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)
    emergency_contact_name = models.CharField(max_length=100, blank=True)
    emergency_contact_phone = models.CharField(max_length=50, blank=True)
    
    # Support Requirements
    primary_disability = models.CharField(max_length=255, blank=True)
    current_situation = models.TextField(blank=True)
    requested_services = models.TextField(blank=True)
    urgency = models.CharField(max_length=20, default='Medium') # Low, Medium, High
    
    # Medical Information
    medical_conditions = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    current_medication = models.TextField(blank=True)
    behaviour_support_required = models.TextField(blank=True)
    risk_information = models.TextField(blank=True)

    # Additional Notes
    referral_notes = models.TextField(blank=True)
    attachments = models.FileField(upload_to='referrals/', blank=True, null=True)
    consent_received = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.referral_id:
            last_ref = Referral.objects.all().order_by('id').last()
            if not last_ref:
                self.referral_id = 'REF-0001'
            else:
                last_id = int(last_ref.referral_id.split('-')[1])
                self.referral_id = f'REF-{last_id + 1:04d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at.strftime('%Y-%m-%d')}"

class ReferralService(models.Model):
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE, related_name='services_required')
    service_name = models.CharField(max_length=150)

    def __str__(self):
        return self.service_name

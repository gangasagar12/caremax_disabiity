from django.db import models

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
        ('In Progress', 'In Progress'),
        ('Approved', 'Approved'),
        ('Closed', 'Closed'),
    )

    # Participant Details
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True, verbose_name="Address / Suburb")
    ndis_number = models.CharField(max_length=50, blank=True, verbose_name="NDIS Number")
    plan_management = models.CharField(max_length=50, choices=PLAN_MANAGEMENT_CHOICES, blank=True, verbose_name="Plan Managed By")

    # Support Information
    support_goals = models.TextField(blank=True)
    additional_notes = models.TextField(blank=True)

    # Referrer Information
    referrer_name = models.CharField(max_length=150, blank=True)
    relationship = models.CharField(max_length=50, choices=RELATIONSHIP_CHOICES, blank=True)
    referrer_phone = models.CharField(max_length=20, blank=True)
    referrer_email = models.EmailField(blank=True)

    # System Fields
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at.strftime('%Y-%m-%d')}"

class ReferralService(models.Model):
    referral = models.ForeignKey(Referral, on_delete=models.CASCADE, related_name='services_required')
    service_name = models.CharField(max_length=150)

    def __str__(self):
        return self.service_name

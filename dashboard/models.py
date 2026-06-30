from django.db import models
from django.contrib.auth.models import User

class Participant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ndis_number = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    status = models.CharField(
        max_length=20, 
        choices=[('Active', 'Active'), ('Pending', 'Pending'), ('Inactive', 'Inactive')],
        default='Active'
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class SupportWorker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='support_worker_profile')
    employee_id = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(
        max_length=20, 
        choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('On Leave', 'On Leave')],
        default='Active'
    )
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.employee_id})"

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='appointments')
    staff = models.ForeignKey(SupportWorker, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    service_type = models.CharField(max_length=100, default='Core Support')
    duration_minutes = models.IntegerField(default=60)
    recurring = models.CharField(max_length=20, choices=[('None', 'None'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], default='None')
    special_instructions = models.TextField(blank=True, null=True)
    medical_alerts = models.TextField(blank=True, null=True)
    support_notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.participant} - {self.date} with {self.staff}"

class VisitRecord(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='visit_record')
    check_in_time = models.DateTimeField(null=True, blank=True)
    check_out_time = models.DateTimeField(null=True, blank=True)
    care_notes = models.TextField(blank=True, null=True)
    admin_reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visit for {self.appointment}"

class VisitDocument(models.Model):
    visit = models.ForeignKey(VisitRecord, on_delete=models.CASCADE, related_name='documents')
    file_upload = models.FileField(upload_to='visit_docs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Doc for {self.visit}"

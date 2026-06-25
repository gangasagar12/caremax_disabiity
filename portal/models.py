from django.db import models
from django.contrib.auth.models import User

# Add a helper property to the User model so Jazzmin can easily get the avatar
@property
def get_avatar_url(self):
    if hasattr(self, 'staff_profile') and self.staff_profile.profile_picture:
        return self.staff_profile.profile_picture.url
    return None

User.add_to_class('avatar_url', get_avatar_url)

class StaffProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Staff', 'Staff'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='staff_profile')
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Staff')
    profile_picture = models.ImageField(upload_to='staff_profiles/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.role}"

class Participant(models.Model):
    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Pending', 'Pending'),
        ('Archived', 'Archived'),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    ndis_number = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    assigned_staff = models.ManyToManyField(User, related_name='assigned_participants', blank=True)
    
    # Details
    emergency_contacts = models.TextField(blank=True)
    ndis_information = models.TextField(blank=True)
    support_needs = models.TextField(blank=True)
    medical_notes = models.TextField(blank=True)
    communication_preferences = models.TextField(blank=True)
    goals_and_outcomes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.ndis_number})"

class SupportPlan(models.Model):
    CATEGORY_CHOICES = (
        ('Daily Life Assistance', 'Daily Life Assistance'),
        ('Household Tasks', 'Household Tasks'),
        ('Travel & Transport', 'Travel & Transport'),
        ('Social & Community', 'Social & Community'),
        ('Shared Living & SIL', 'Shared Living & SIL'),
        ('Group Activities', 'Group Activities'),
        ('Life Skills Development', 'Life Skills Development'),
        ('Employment & Education', 'Employment & Education'),
    )
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='support_plans')
    goals = models.TextField()
    support_categories = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    service_frequency = models.CharField(max_length=100)
    review_date = models.DateField()
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plan for {self.participant} - {self.support_categories}"

class CaseNote(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='case_notes')
    staff_member = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='case_notes')
    date = models.DateField(auto_now_add=True)
    note_type = models.CharField(max_length=100)
    details = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note by {self.staff_member} on {self.date}"

class Document(models.Model):
    TYPE_CHOICES = (
        ('NDIS Plan', 'NDIS Plan'),
        ('Service Agreement', 'Service Agreement'),
        ('Support Plan', 'Support Plan'),
        ('Report', 'Report'),
        ('Assessment', 'Assessment'),
        ('Medical Document', 'Medical Document'),
        ('Consent Form', 'Consent Form'),
        ('Other', 'Other'),
    )
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='documents')
    title = models.CharField(max_length=200)
    document_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    file = models.FileField(upload_to='participant_documents/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.participant}"

class LeaveRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    staff = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leave_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    admin_comment = models.TextField(blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Leave for {self.staff} ({self.start_date} to {self.end_date})"

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='activity_logs')
    action = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.action} at {self.timestamp}"

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Notification for {self.user} - {self.title}"

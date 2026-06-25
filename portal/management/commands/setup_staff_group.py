from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from portal.models import Participant, SupportPlan, CaseNote, Document, LeaveRequest, Announcement
from referrals.models import Referral

class Command(BaseCommand):
    help = 'Creates the Staff Group and assigns appropriate permissions'

    def handle(self, *args, **options):
        # Create or get the Staff Group
        staff_group, created = Group.objects.get_or_create(name='Staff Group')
        
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created Staff Group'))
        else:
            self.stdout.write(self.style.WARNING('Staff Group already exists, updating permissions...'))
            
        # Models that Staff can view, add, change (but NOT delete)
        target_models = [
            Participant, SupportPlan, CaseNote, Document, LeaveRequest, Referral
        ]
        
        # Clear existing permissions to avoid conflicts
        staff_group.permissions.clear()
        
        permissions_added = 0
        for model in target_models:
            content_type = ContentType.objects.get_for_model(model)
            # Find view, add, change permissions
            permissions = Permission.objects.filter(
                content_type=content_type,
                codename__in=[
                    f'view_{model._meta.model_name}',
                    f'add_{model._meta.model_name}',
                    f'change_{model._meta.model_name}'
                ]
            )
            for perm in permissions:
                staff_group.permissions.add(perm)
                permissions_added += 1
                
        # Handle Announcements (view only)
        announcement_ct = ContentType.objects.get_for_model(Announcement)
        try:
            view_announcement_perm = Permission.objects.get(
                content_type=announcement_ct,
                codename='view_announcement'
            )
            staff_group.permissions.add(view_announcement_perm)
            permissions_added += 1
        except Permission.DoesNotExist:
            pass

        self.stdout.write(self.style.SUCCESS(f'Successfully assigned {permissions_added} permissions to Staff Group.'))

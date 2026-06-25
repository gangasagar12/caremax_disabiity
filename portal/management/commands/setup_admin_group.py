from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Creates the Admin Group and assigns all appropriate permissions'

    def handle(self, *args, **options):
        # Create or get the Admin Group
        admin_group, created = Group.objects.get_or_create(name='Admin Group')
        
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created Admin Group'))
        else:
            self.stdout.write(self.style.WARNING('Admin Group already exists, updating permissions...'))
            
        # For an Admin Group, we typically want them to have access to almost everything in the system,
        # but to be safe and explicit, let's grab all permissions for portal and referral apps.
        # Alternatively, a simpler way is to just assign all permissions except auth ones.
        # But let's just assign ALL permissions for all installed content types as they are Admins.
        
        all_perms = Permission.objects.all()
        admin_group.permissions.set(all_perms)

        self.stdout.write(self.style.SUCCESS(f'Successfully assigned {all_perms.count()} permissions to Admin Group.'))

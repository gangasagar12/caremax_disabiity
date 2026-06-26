from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from guardian.shortcuts import assign_perm, remove_perm
from .models import Participant, StaffProfile
from referrals.models import Referral

# Sync StaffProfile with Django Groups
@receiver(post_save, sender=StaffProfile)
def sync_staff_profile_group(sender, instance, created, **kwargs):
    user = instance.user
    
    # Remove from both groups first to ensure clean state
    try:
        admin_group = Group.objects.get(name='Admin Group')
        user.groups.remove(admin_group)
    except Group.DoesNotExist:
        pass
        
    try:
        staff_group = Group.objects.get(name='Staff Group')
        user.groups.remove(staff_group)
    except Group.DoesNotExist:
        pass
        
    # Add to appropriate group
    if instance.role == 'Admin':
        try:
            admin_group = Group.objects.get(name='Admin Group')
            user.groups.add(admin_group)
        except Group.DoesNotExist:
            pass
    elif instance.role == 'Staff':
        try:
            staff_group = Group.objects.get(name='Staff Group')
            user.groups.add(staff_group)
        except Group.DoesNotExist:
            pass

# Sync Participant assigned_staff with Guardian Object-Level Permissions
@receiver(m2m_changed, sender=Participant.assigned_staff.through)
def sync_participant_permissions(sender, instance, action, pk_set, **kwargs):
    if action == 'post_add':
        for user_id in pk_set:
            user = User.objects.get(pk=user_id)
            assign_perm('view_participant', user, instance)
            assign_perm('change_participant', user, instance)
    elif action == 'post_remove':
        for user_id in pk_set:
            user = User.objects.get(pk=user_id)
            remove_perm('view_participant', user, instance)
            remove_perm('change_participant', user, instance)
    elif action == 'post_clear':
        # If all assigned staff are cleared, remove permissions for everyone who is not a superuser/admin
        # (This is more complex, usually we just let it be or remove all explicit perms for this obj)
        from guardian.models import UserObjectPermission
        UserObjectPermission.objects.filter(object_pk=instance.pk).delete()

# Sync Referral assigned_staff with Guardian Object-Level Permissions
@receiver(post_save, sender=Referral)
def sync_referral_permissions(sender, instance, created, **kwargs):
    from guardian.models import UserObjectPermission
    # Remove existing explicit object permissions for this referral
    UserObjectPermission.objects.filter(
        content_type__model='referral', 
        object_pk=instance.pk
    ).delete()
    
    # Assign permission to the current staff member
    if instance.assigned_staff:
        assign_perm('view_referral', instance.assigned_staff, instance)
        assign_perm('change_referral', instance.assigned_staff, instance)

from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, group_name):
    """
    Check if a user belongs to a specific group.
    Returns True if user is a superuser OR in the group.
    Usage in templates: {% if request.user|has_group:"Admin Group" %}
    """
    if not user.is_authenticated:
        return False
        
    if user.is_superuser:
        return True
        
    return user.groups.filter(name=group_name).exists()

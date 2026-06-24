from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import StaffProfile

# Define an inline admin descriptor for StaffProfile model
# which acts a bit like a singleton
class StaffProfileInline(admin.StackedInline):
    model = StaffProfile
    can_delete = False
    verbose_name_plural = 'Staff Profile Picture & Details'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (StaffProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


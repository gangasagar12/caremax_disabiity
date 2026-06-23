from django.contrib import admin
from .models import Referral, ReferralService

class ReferralServiceInline(admin.TabularInline):
    model = ReferralService
    extra = 0

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'plan_management', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'plan_management')
    search_fields = ('first_name', 'last_name', 'ndis_number', 'email', 'phone')
    inlines = [ReferralServiceInline]
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('Participant Details', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'gender', 'phone', 'email', 'address', 'ndis_number', 'plan_management')
        }),
        ('Support Information', {
            'fields': ('support_goals', 'additional_notes')
        }),
        ('Referrer Details', {
            'fields': ('referrer_name', 'relationship', 'referrer_phone', 'referrer_email')
        }),
        ('System Info', {
            'fields': ('status', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

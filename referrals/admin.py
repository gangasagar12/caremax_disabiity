from django.contrib import admin
from .models import Referral, ReferralService

class ReferralServiceInline(admin.TabularInline):
    model = ReferralService
    extra = 0

@admin.register(Referral)
class ReferralAdmin(admin.ModelAdmin):
    list_display = ('referral_id', 'first_name', 'last_name', 'referral_source', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'urgency')
    search_fields = ('first_name', 'last_name', 'referral_id', 'email', 'phone')
    inlines = [ReferralServiceInline]
    readonly_fields = ('created_at', 'updated_at')

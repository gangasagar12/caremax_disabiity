from django.contrib import admin
from .models import ServiceCategory, Service, ServiceFeature, ServiceBenefit, ServiceFAQ

class ServiceFeatureInline(admin.StackedInline):
    model = ServiceFeature
    extra = 1

class ServiceBenefitInline(admin.StackedInline):
    model = ServiceBenefit
    extra = 1

class ServiceFAQInline(admin.StackedInline):
    model = ServiceFAQ
    extra = 1

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_at')
    list_filter = ('category', 'status')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceFeatureInline, ServiceBenefitInline, ServiceFAQInline]

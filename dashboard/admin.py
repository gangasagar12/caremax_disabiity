from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.db.models import Count
from django.utils import timezone
from referrals.models import Referral
from resources.models import Blog
from contact.models import ContactMessage

class CustomAdminSite(AdminSite):
    site_header = "CareMax Disability Administration"
    site_title = "CareMax Admin"
    index_title = "Operations Dashboard"

    def index(self, request, extra_context=None):
        # Gather analytics data
        total_participants = Referral.objects.filter(status='Approved').count()
        new_referrals_count = Referral.objects.filter(status='New').count()
        active_staff = User.objects.filter(is_active=True, is_staff=True).count()
        contact_messages_count = ContactMessage.objects.filter(is_resolved=False).count()
        published_blogs_count = Blog.objects.filter(is_published=True).count()
        open_jobs_count = 0  # Mocked as there is no Job model yet

        # Gather lists
        recent_referrals = Referral.objects.order_by('-created_at')[:5]
        recent_messages = ContactMessage.objects.order_by('-created_at')[:5]
        recent_blogs = Blog.objects.order_by('-created_at')[:5]

        # Context injection
        app_list = self.get_app_list(request)
        context = {
            **self.each_context(request),
            'title': self.index_title,
            'subtitle': None,
            'app_list': app_list,
            'total_participants': total_participants,
            'new_referrals_count': new_referrals_count,
            'active_staff': active_staff,
            'contact_messages_count': contact_messages_count,
            'published_blogs_count': published_blogs_count,
            'open_jobs_count': open_jobs_count,
            'recent_referrals': recent_referrals,
            'recent_messages': recent_messages,
            'recent_blogs': recent_blogs,
            **(extra_context or {}),
        }
        
        request.current_app = self.name
        
        # We override the template to point to our custom index
        from django.template.response import TemplateResponse
        return TemplateResponse(request, "dashboard/index.html", context)

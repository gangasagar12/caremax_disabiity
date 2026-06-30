from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "core/home.html"
    
class AboutView(TemplateView):
    template_name = "core/about.html"

from django.contrib.auth.views import LoginView

class RoleBasedLoginView(LoginView):
    def get_success_url(self):
        role = self.request.POST.get('login_role')
        if role == 'admin':
            return '/dashboard/'
        elif role == 'staff':
            return '/staff/'
        elif role == 'coordinator':
            return '/staff/'  # Temporary fallback for coordinator
        return super().get_success_url()

from django.shortcuts import redirect
from django.urls import reverse

class PortalSeparationMiddleware:
    """
    Middleware to ensure that users accessing the /portal/ must have 
    explicitly logged in through the portal login page. 
    A session from /admin/ will not automatically grant access to /portal/ 
    without the 'portal_logged_in' session flag.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path
        
        # Check if the request is targeting the portal
        if path.startswith('/portal/'):
            # Allow access to login and logout without restrictions
            allowed_paths = [
                reverse('portal:login'),
                reverse('portal:logout'),
            ]
            
            if path not in allowed_paths:
                # If they are authenticated globally but lack the portal-specific session flag
                if request.user.is_authenticated and not request.session.get('portal_logged_in'):
                    return redirect('portal:login')

        response = self.get_response(request)
        return response

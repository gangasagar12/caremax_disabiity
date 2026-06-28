class AdminRememberMeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        # Check if the user just logged in via admin and checked "remember_me"
        if request.path == '/admin/login/' and request.method == 'POST':
            if request.user.is_authenticated and request.POST.get('remember_me'):
                request.session.set_expiry(1209600)  # 2 weeks
            elif request.user.is_authenticated and not request.POST.get('remember_me'):
                request.session.set_expiry(0) # Expire on browser close
        return response

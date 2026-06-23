from services.models import Service

def global_services(request):
    """
    Makes all active services available to all templates (e.g., for the mega menu).
    """
    return {
        'global_services': Service.objects.filter(status=True).order_by('title')
    }

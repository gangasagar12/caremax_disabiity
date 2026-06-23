import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from services.models import ServiceCategory, Service, ServiceFeature, ServiceFAQ, ServiceBenefit

def seed():
    # Service Data
    services_data = [
        {
            "slug": "personal-care",
            "benefits": [
                {"title": "Increased Independence", "desc": "Live more autonomously with respectful support.", "icon": "fas fa-walking"},
                {"title": "Improved Quality of Life", "desc": "Enhance your daily wellbeing and comfort.", "icon": "fas fa-smile"},
                {"title": "Enhanced Confidence", "desc": "Feel assured in your daily routines and personal care.", "icon": "fas fa-star"},
                {"title": "Personalised Support", "desc": "Care designed exactly for your unique needs.", "icon": "fas fa-user-check"}
            ],
        },
        {
            "slug": "household-tasks",
            "benefits": [
                {"title": "Safe Environment", "desc": "Maintain a clean, hazard-free living space.", "icon": "fas fa-shield-alt"},
                {"title": "More Free Time", "desc": "Focus on what you love while we handle the chores.", "icon": "fas fa-clock"},
                {"title": "Reduced Stress", "desc": "Enjoy peace of mind in a well-managed home.", "icon": "fas fa-spa"}
            ]
        },
        {
            "slug": "community-participation",
            "benefits": [
                {"title": "Social Connection", "desc": "Build meaningful friendships and networks.", "icon": "fas fa-users"},
                {"title": "Skill Building", "desc": "Learn new hobbies and social skills.", "icon": "fas fa-book-reader"},
                {"title": "Community Inclusion", "desc": "Feel an active part of your local community.", "icon": "fas fa-hands-helping"}
            ]
        },
        {
            "slug": "supported-independent-living",
            "benefits": [
                {"title": "24/7 Security", "desc": "Peace of mind with round-the-clock available support.", "icon": "fas fa-lock"},
                {"title": "Life Skills", "desc": "Gain crucial skills for independent living.", "icon": "fas fa-chart-line"},
                {"title": "Comfortable Living", "desc": "A home environment tailored to your needs.", "icon": "fas fa-couch"}
            ]
        }
    ]

    for data in services_data:
        try:
            service = Service.objects.get(slug=data['slug'])
            # Clear old to prevent duplicates if run multiple times
            ServiceBenefit.objects.filter(service=service).delete()
            for ben in data['benefits']:
                ServiceBenefit.objects.create(service=service, title=ben['title'], description=ben['desc'], icon=ben['icon'])
            print(f"Added benefits to: {service.title}")
        except Service.DoesNotExist:
            print(f"Skipping {data['slug']}, service not found.")

if __name__ == '__main__':
    seed()
    print("Database benefits seeded successfully!")

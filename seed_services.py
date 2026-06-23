import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from services.models import ServiceCategory, Service, ServiceFeature, ServiceFAQ

def seed():
    # Create Categories
    cat_daily = ServiceCategory.objects.create(title="Daily Support", slug="daily-support")
    cat_community = ServiceCategory.objects.create(title="Community Access", slug="community-access")
    cat_accommodation = ServiceCategory.objects.create(title="Accommodation", slug="accommodation")

    # Service Data
    services_data = [
        {
            "title": "Personal Care",
            "slug": "personal-care",
            "category": cat_daily,
            "icon": "fas fa-user-nurse",
            "short_description": "Compassionate assistance with daily personal routines, ensuring comfort and dignity.",
            "full_description": "Our Personal Care service provides sensitive and respectful support for your daily routines. From morning preparations to evening wind-downs, our trained professionals assist with hygiene, dressing, and personal maintenance, ensuring you feel confident and comfortable throughout your day.",
            "features": [
                {"title": "Hygiene Assistance", "desc": "Support with showering, bathing, and grooming routines.", "icon": "fas fa-shower"},
                {"title": "Dressing Support", "desc": "Help with morning and evening clothing preparation.", "icon": "fas fa-tshirt"},
                {"title": "Mobility Support", "desc": "Safe assistance with moving around your home.", "icon": "fas fa-walking"}
            ],
            "faqs": [
                {"q": "Can I choose my support worker?", "a": "Yes, we always strive to match you with a worker you feel comfortable with."},
                {"q": "Is support available 24/7?", "a": "Yes, personal care can be arranged around the clock based on your NDIS plan."}
            ]
        },
        {
            "title": "Household Tasks",
            "slug": "household-tasks",
            "category": cat_daily,
            "icon": "fas fa-home",
            "short_description": "Help with cleaning, cooking, and maintaining a safe and healthy home environment.",
            "full_description": "Maintaining a home can be overwhelming, but our team is here to help. We assist with cleaning, laundry, meal preparation, and general home upkeep so you can enjoy a safe, organized, and stress-free living environment.",
            "features": [
                {"title": "Cleaning & Laundry", "desc": "Assistance with keeping your home spotless and managing laundry.", "icon": "fas fa-broom"},
                {"title": "Meal Preparation", "desc": "Cooking nutritious and delicious meals suited to your diet.", "icon": "fas fa-utensils"}
            ],
            "faqs": [
                {"q": "Do you bring your own cleaning supplies?", "a": "Usually we use your preferred supplies to avoid allergies, but we can provide our own if requested."}
            ]
        },
        {
            "title": "Community Participation",
            "slug": "community-participation",
            "category": cat_community,
            "icon": "fas fa-users",
            "short_description": "Support to engage in social activities, hobbies, and local community events.",
            "full_description": "Stay connected and engaged with the world around you. We provide the support you need to attend social events, join clubs, pursue hobbies, or simply enjoy a coffee with friends, fostering a strong sense of belonging.",
            "features": [
                {"title": "Social Outings", "desc": "Assistance attending community events or visiting friends.", "icon": "fas fa-coffee"},
                {"title": "Hobby Support", "desc": "Help participating in classes, sports, or creative groups.", "icon": "fas fa-paint-brush"}
            ],
            "faqs": [
                {"q": "Do you cover the cost of activities?", "a": "NDIS typically covers the support worker's time; activity costs are usually out-of-pocket."}
            ]
        },
        {
            "title": "Supported Independent Living (SIL)",
            "slug": "supported-independent-living",
            "category": cat_accommodation,
            "icon": "fas fa-house-user",
            "short_description": "Comprehensive daily support to help you live independently in your own home.",
            "full_description": "Supported Independent Living (SIL) provides you with the daily support needed to live as independently as possible. Whether in a shared home or your own place, our staff provide assistance with daily tasks while helping you build vital life skills.",
            "features": [
                {"title": "24/7 Care Options", "desc": "Round-the-clock support availability.", "icon": "fas fa-clock"},
                {"title": "Skill Building", "desc": "Learning to cook, budget, and manage a household.", "icon": "fas fa-chart-line"}
            ],
            "faqs": [
                {"q": "Do you help find SIL accommodation?", "a": "Yes, we can assist you in finding suitable shared living arrangements."}
            ]
        }
    ]

    for data in services_data:
        service, created = Service.objects.get_or_create(
            slug=data['slug'],
            defaults={
                'title': data['title'],
                'category': data['category'],
                'icon': data['icon'],
                'short_description': data['short_description'],
                'full_description': data['full_description'],
            }
        )
        if created:
            for feat in data['features']:
                ServiceFeature.objects.create(service=service, title=feat['title'], description=feat['desc'], icon=feat['icon'])
            for faq in data['faqs']:
                ServiceFAQ.objects.create(service=service, question=faq['q'], answer=faq['a'])
            print(f"Created service: {service.title}")

if __name__ == '__main__':
    seed()
    print("Database seeded successfully!")

from django.shortcuts import render
from django.views import View
from django.http import Http404

STATIC_SERVICES = {
    'assistance-with-daily-life': {
        'title': 'Assistance with Daily Life',
        'icon': 'fas fa-hands-helping',
        'short_description': 'Support with daily personal activities to maintain your independence, health, and wellbeing.',
        'full_description': 'Our Assistance with Daily Life services are designed to support you in your own home with everyday tasks. We tailor our approach to respect your routines and preferences, ensuring you live as independently as possible. This includes help with personal care, meal preparation, hygiene, and daily routines.',
    },
    'household-tasks': {
        'title': 'Household Tasks',
        'icon': 'fas fa-home',
        'short_description': 'Reliable support with cleaning, laundry, meal preparation, and general home maintenance tasks.',
        'full_description': 'We provide practical support around the home so you can maintain a clean, safe, and comfortable living environment. Our support workers can assist with domestic chores such as cleaning, dishwashing, laundry, ironing, and basic property maintenance.',
    },
    'travel-and-transport': {
        'title': 'Travel & Transport',
        'icon': 'fas fa-car',
        'short_description': 'Safe and dependable transport for medical appointments, shopping, and community outings.',
        'full_description': 'Navigating the community shouldn\'t be a barrier. Our travel and transport services ensure you can get to where you need to be safely and reliably. Whether it’s attending medical appointments, going to work, or participating in social events, we offer dedicated transport support.',
    },
    'social-and-community-participation': {
        'title': 'Social & Community Participation',
        'icon': 'fas fa-users',
        'short_description': 'Engage actively in social events, community activities, and recreational pursuits.',
        'full_description': 'Staying connected to the community is vital for wellbeing. We support you to participate actively in social, civic, and recreational activities. From joining a local club or hobby group to attending community events, we’re here to help you build meaningful relationships and enjoy your community.',
    },
    'shared-living-and-sil': {
        'title': 'Shared Living & SIL',
        'icon': 'fas fa-bed',
        'short_description': 'Dedicated assistance to live independently and comfortably in shared accommodation.',
        'full_description': 'Supported Independent Living (SIL) provides you with the help you need to live independently, whether in your own home or in shared accommodation. Our dedicated team is available to assist with daily tasks, building your skills, and ensuring you have a supportive and empowering home environment.',
    },
    'group-and-centre-activities': {
        'title': 'Group & Centre Activities',
        'icon': 'fas fa-layer-group',
        'short_description': 'Join inclusive group programs and centre-based activities tailored to your interests.',
        'full_description': 'Our group and centre-based activities offer a fantastic way to meet new people, learn new skills, and have fun in a supportive environment. We organize a variety of workshops, social gatherings, and developmental programs tailored to the interests and goals of our participants.',
    },
    'daily-living-skills': {
        'title': 'Daily Living Skills',
        'icon': 'fas fa-graduation-cap',
        'short_description': 'Developmental programs designed to build your capacity, confidence, and life skills.',
        'full_description': 'We believe in empowering you to achieve your goals. Our life skills development programs are focused on building your independence and capacity to manage daily life. We offer training in areas such as financial management, public transport training, cooking, and personal growth.',
    },
    'employment-and-education-support': {
        'title': 'Employment & Education Support',
        'icon': 'fas fa-briefcase',
        'short_description': 'Guidance and assistance to pursue meaningful employment or educational pathways.',
        'full_description': 'Achieving your career and educational aspirations is important to us. We provide tailored support to help you transition into employment or higher education. This includes resume building, interview preparation, workplace assistance, and guidance in navigating educational institutions.',
    }
}

class ServiceListView(View):
    def get(self, request):
        return render(request, 'services/service_list.html')

class ServiceDetailView(View):
    def get(self, request, slug):
        service = STATIC_SERVICES.get(slug)
        if not service:
            raise Http404("Service not found")
            
        service_copy = service.copy()
        service_copy['slug'] = slug
            
        related_services = []
        for k, s in STATIC_SERVICES.items():
            if k != slug:
                s_copy = s.copy()
                s_copy['slug'] = k
                related_services.append(s_copy)
                if len(related_services) >= 3:
                    break
        
        context = {
            'service': service_copy,
            'related_services': related_services,
        }
        return render(request, 'services/service_detail.html', context)

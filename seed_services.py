import os

services = [
    {
        'slug': 'assistance-with-daily-life',
        'title': 'Assistance with Daily Life',
        'icon': 'fas fa-hands-helping',
        'short': 'Support with daily personal activities to maintain your independence, health, and wellbeing.',
        'full': 'Our Assistance with Daily Life services are designed to support you in your own home with everyday tasks. We tailor our approach to respect your routines and preferences, ensuring you live as independently as possible. This includes help with personal care, meal preparation, hygiene, and daily routines.',
        'features': [
            {'icon': 'fas fa-shower', 'title': 'Personal Hygiene', 'desc': 'Assistance with showering, dressing, and grooming.'},
            {'icon': 'fas fa-utensils', 'title': 'Meal Preparation', 'desc': 'Help with planning and preparing nutritious meals.'},
            {'icon': 'fas fa-notes-medical', 'title': 'Medication Assistance', 'desc': 'Prompting and assisting with medication management.'}
        ],
        'faqs': [
            {'q': 'Can I choose my support worker?', 'a': 'Yes, we match you with support workers based on your preferences and needs.'},
            {'q': 'Is support available 24/7?', 'a': 'We offer flexible support options, including 24/7 care if required by your plan.'}
        ]
    },
    {
        'slug': 'household-tasks',
        'title': 'Household Tasks',
        'icon': 'fas fa-home',
        'short': 'Reliable support with cleaning, laundry, meal preparation, and general home maintenance tasks.',
        'full': 'We provide practical support around the home so you can maintain a clean, safe, and comfortable living environment. Our support workers can assist with domestic chores such as cleaning, dishwashing, laundry, ironing, and basic property maintenance.',
        'features': [
            {'icon': 'fas fa-broom', 'title': 'General Cleaning', 'desc': 'Vacuuming, mopping, and dusting to keep your home fresh.'},
            {'icon': 'fas fa-tshirt', 'title': 'Laundry Services', 'desc': 'Washing, drying, ironing, and folding clothes.'},
            {'icon': 'fas fa-shopping-basket', 'title': 'Grocery Shopping', 'desc': 'Assistance with shopping and putting away groceries.'}
        ],
        'faqs': [
            {'q': 'Do I need to provide cleaning supplies?', 'a': 'Generally, yes, our workers will use your preferred supplies, but we can arrange alternatives if needed.'},
            {'q': 'How often can someone come to clean?', 'a': 'Frequency depends entirely on your NDIS plan and personal needs.'}
        ]
    },
    {
        'slug': 'travel-and-transport',
        'title': 'Travel & Transport',
        'icon': 'fas fa-car',
        'short': 'Safe and dependable transport for medical appointments, shopping, and community outings.',
        'full': 'Navigating the community shouldn\'t be a barrier. Our travel and transport services ensure you can get to where you need to be safely and reliably. Whether it’s attending medical appointments, going to work, or participating in social events, we offer dedicated transport support.',
        'features': [
            {'icon': 'fas fa-hospital-user', 'title': 'Medical Appointments', 'desc': 'Reliable transport to and from doctors or therapy sessions.'},
            {'icon': 'fas fa-shopping-cart', 'title': 'Shopping Trips', 'desc': 'Assistance getting to the shops and transporting goods.'},
            {'icon': 'fas fa-bus', 'title': 'Public Transport Training', 'desc': 'Building skills and confidence to use public transport independently.'}
        ],
        'faqs': [
            {'q': 'Are your vehicles wheelchair accessible?', 'a': 'Yes, we have access to modified vehicles for wheelchair users.'},
            {'q': 'Will the driver wait for me at my appointment?', 'a': 'Yes, we can arrange for the support worker to wait and assist you returning home.'}
        ]
    },
    {
        'slug': 'social-and-community-participation',
        'title': 'Social & Community Participation',
        'icon': 'fas fa-users',
        'short': 'Engage actively in social events, community activities, and recreational pursuits.',
        'full': 'Staying connected to the community is vital for wellbeing. We support you to participate actively in social, civic, and recreational activities. From joining a local club or hobby group to attending community events, we’re here to help you build meaningful relationships and enjoy your community.',
        'features': [
            {'icon': 'fas fa-user-friends', 'title': 'Social Outings', 'desc': 'Going to cafes, movies, or community events.'},
            {'icon': 'fas fa-palette', 'title': 'Hobbies & Interests', 'desc': 'Support to join clubs, classes, or recreational groups.'},
            {'icon': 'fas fa-hands-helping', 'title': 'Community Engagement', 'desc': 'Volunteering or participating in local community programs.'}
        ],
        'faqs': [
            {'q': 'Can you help me find a new hobby?', 'a': 'Absolutely! We love helping participants explore new interests and find groups.'},
            {'q': 'Is the cost of the activity covered?', 'a': 'The NDIS typically covers the support worker’s time, while you may need to cover your ticket or entry fee.'}
        ]
    },
    {
        'slug': 'shared-living-and-sil',
        'title': 'Shared Living & SIL',
        'icon': 'fas fa-bed',
        'short': 'Dedicated assistance to live independently and comfortably in shared accommodation.',
        'full': 'Supported Independent Living (SIL) provides you with the help you need to live independently, whether in your own home or in shared accommodation. Our dedicated team is available to assist with daily tasks, building your skills, and ensuring you have a supportive and empowering home environment.',
        'features': [
            {'icon': 'fas fa-house-user', 'title': 'Accommodation Support', 'desc': 'Assistance living in shared housing with tailored support.'},
            {'icon': 'fas fa-tasks', 'title': 'Daily Routine Help', 'desc': 'Support with cooking, cleaning, and personal care.'},
            {'icon': 'fas fa-comments', 'title': 'Mediation & Harmony', 'desc': 'Helping build positive relationships with housemates.'}
        ],
        'faqs': [
            {'q': 'What is SIL?', 'a': 'Supported Independent Living refers to help with daily tasks in a shared living environment.'},
            {'q': 'Can you help me find a SIL vacancy?', 'a': 'Yes, we can assist you in finding suitable accommodation that meets your needs.'}
        ]
    },
    {
        'slug': 'group-and-centre-activities',
        'title': 'Group & Centre Activities',
        'icon': 'fas fa-layer-group',
        'short': 'Join inclusive group programs and centre-based activities tailored to your interests.',
        'full': 'Our group and centre-based activities offer a fantastic way to meet new people, learn new skills, and have fun in a supportive environment. We organize a variety of workshops, social gatherings, and developmental programs tailored to the interests and goals of our participants.',
        'features': [
            {'icon': 'fas fa-paint-brush', 'title': 'Creative Workshops', 'desc': 'Art, music, and craft sessions.'},
            {'icon': 'fas fa-dumbbell', 'title': 'Fitness Groups', 'desc': 'Gentle exercise, yoga, and physical wellbeing programs.'},
            {'icon': 'fas fa-chalkboard-teacher', 'title': 'Skill Building', 'desc': 'Group cooking classes or computer skills training.'}
        ],
        'faqs': [
            {'q': 'Are activities held at a specific centre?', 'a': 'We run activities both at our dedicated centre and out in the community.'},
            {'q': 'How many people are in a group?', 'a': 'Groups vary in size, but we keep them small enough to ensure everyone gets adequate attention.'}
        ]
    },
    {
        'slug': 'daily-living-skills',
        'title': 'Daily Living Skills',
        'icon': 'fas fa-graduation-cap',
        'short': 'Developmental programs designed to build your capacity, confidence, and life skills.',
        'full': 'We believe in empowering you to achieve your goals. Our life skills development programs are focused on building your independence and capacity to manage daily life. We offer training in areas such as financial management, public transport training, cooking, and personal growth.',
        'features': [
            {'icon': 'fas fa-wallet', 'title': 'Financial Management', 'desc': 'Learning to budget, pay bills, and handle money.'},
            {'icon': 'fas fa-utensils', 'title': 'Cooking Skills', 'desc': 'Planning meals, shopping, and safe cooking techniques.'},
            {'icon': 'fas fa-comments', 'title': 'Communication Skills', 'desc': 'Building confidence in social and formal communication.'}
        ],
        'faqs': [
            {'q': 'Is the training one-on-one?', 'a': 'Yes, we provide individualised training tailored to your learning style and goals.'},
            {'q': 'How long does skill development take?', 'a': 'It depends entirely on the skill and the individual. We move at your pace.'}
        ]
    },
    {
        'slug': 'employment-and-education-support',
        'title': 'Employment & Education Support',
        'icon': 'fas fa-briefcase',
        'short': 'Guidance and assistance to pursue meaningful employment or educational pathways.',
        'full': 'Achieving your career and educational aspirations is important to us. We provide tailored support to help you transition into employment or higher education. This includes resume building, interview preparation, workplace assistance, and guidance in navigating educational institutions.',
        'features': [
            {'icon': 'fas fa-file-alt', 'title': 'Resume Building', 'desc': 'Help writing professional resumes and cover letters.'},
            {'icon': 'fas fa-user-tie', 'title': 'Interview Prep', 'desc': 'Coaching and practice for job interviews.'},
            {'icon': 'fas fa-school', 'title': 'Study Support', 'desc': 'Assistance enrolling in courses and managing study loads.'}
        ],
        'faqs': [
            {'q': 'Do you guarantee a job?', 'a': 'While we cannot guarantee employment, we provide all the tools and support to maximize your chances.'},
            {'q': 'Can you support me at work?', 'a': 'Yes, we can provide on-the-job support to help you settle in and manage your tasks.'}
        ]
    }
]

template_string = """{% extends 'base.html' %}
{% load static %}

{% block title %}{title} | Support Services{% endblock %}

{% block content %}
<!-- 1. SERVICE HERO SECTION -->
<section class="service-detail-hero section-padding" style="background-image: linear-gradient(rgba(15, 74, 104, 0.85), rgba(15, 74, 104, 0.85)), url('{% static "images/about_hero.png" %}'); background-size: cover; background-position: center; color: var(--white);">
    <div class="container text-center">
        <div class="breadcrumbs mb-3">
            <a href="/">Home</a> &gt; <a href="{% url 'services:service_list' %}">Services</a> &gt; <span>{title}</span>
        </div>
        <h1 class="section-title text-white">{title}</h1>
        <p class="section-subtitle mx-auto max-w-700 text-white-50">{short}</p>
    </div>
</section>

<!-- 2. ABOUT THE SERVICE -->
<section class="service-overview section-padding bg-light">
    <div class="container">
        <div class="about-service-flex">
            <div class="about-service-image">
                <img src="{% static 'images/team.png' %}" alt="{title}" class="rounded-image shadow">
            </div>
            <div class="about-service-content">
                <h2 class="mb-4">About {title}</h2>
                <p style="font-size: 1.1rem; line-height: 1.8;">{full}</p>
            </div>
        </div>
    </div>
</section>

<!-- 3. HOW WE HELP -->
<section class="service-features section-padding">
    <div class="container">
        <h2 class="text-center section-title">How We Help</h2>
        <div class="features-grid mt-4">
            {features_html}
        </div>
    </div>
</section>

<!-- 4. FREQUENTLY ASKED QUESTIONS -->
<section class="service-faqs section-padding">
    <div class="container max-w-700 mx-auto">
        <h2 class="text-center section-title mb-4">Frequently Asked Questions</h2>
        <div class="faq-accordion">
            {faqs_html}
        </div>
    </div>
</section>

<!-- 5. CONTACT CTA -->
<section class="section-padding mb-5">
    <div class="container">
        <div id="contact" class="contact-cta text-center shadow-lg" style="background-color: var(--primary); color: var(--white); padding: 60px 30px; border-radius: 24px;">
            <h2>Ready to Discuss Your Support Needs?</h2>
            <p class="mt-3 mb-4 mx-auto max-w-700" style="color: rgba(255,255,255,0.7);">Contact our dedicated intake team today to discuss how we can tailor this service to your unique goals.</p>
            <div class="hero-buttons">
                <a href="{% url 'contact:contact_us' %}" class="btn btn-outline-light btn-large mr-3">Contact Us</a>
                <a href="{% url 'referrals:referral_create' %}" class="btn bg-white btn-large" style="color: var(--primary);">Get Support Today</a>
            </div>
        </div>
    </div>
</section>
{% endblock content %}
"""

for service in services:
    features_html = ''
    for f in service['features']:
        features_html += f'''<div class="feature-card shadow bg-white">
                <div class="icon-wrapper"><i class="{f['icon']}"></i></div>
                <h4>{f['title']}</h4>
                <p>{f['desc']}</p>
            </div>\n            '''
            
    faqs_html = ''
    for faq in service['faqs']:
        faqs_html += f'''<div class="faq-item shadow bg-white">
                <h4 class="faq-question">{faq['q']}</h4>
                <p class="faq-answer">{faq['a']}</p>
            </div>\n            '''
            
    content = template_string.replace('{title}', service['title'])\
                             .replace('{short}', service['short'])\
                             .replace('{full}', service['full'])\
                             .replace('{features_html}', features_html)\
                             .replace('{faqs_html}', faqs_html)
    
    file_path = f"d:/projects/caraamax/templates/services/{service['slug'].replace('-', '_')}.html"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Successfully created 8 static template files!')

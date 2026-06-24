from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Participant, SupportPlan, CaseNote, Document, LeaveRequest, Announcement
from referrals.models import Referral

def portal_login(request):
    if request.user.is_authenticated:
        return redirect('portal:dashboard')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not request.POST.get('remember_me'):
                request.session.set_expiry(0)
            return redirect('portal:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            
    return render(request, 'portal/login.html')

def portal_logout(request):
    logout(request)
    return redirect('portal:login')

@login_required(login_url='portal:login')
def dashboard(request):
    from django.contrib.auth.models import User
    total_participants = Participant.objects.count()
    active_participants = Participant.objects.filter(status='Active').count()
    new_referrals = Referral.objects.filter(status='New').count()
    pending_referrals = Referral.objects.filter(status__in=['Contacted', 'Assessment Scheduled', 'In Progress']).count()
    active_staff = User.objects.filter(is_active=True).count()
    
    recent_referrals = Referral.objects.all().order_by('-created_at')[:5]
    
    context = {
        'total_participants': total_participants,
        'active_participants': active_participants,
        'new_referrals': new_referrals,
        'pending_referrals': pending_referrals,
        'active_staff': active_staff,
        'recent_referrals': recent_referrals,
    }
    return render(request, 'portal/dashboard.html', context)

@login_required(login_url='portal:login')
def participant_list(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    
    participants = Participant.objects.all().order_by('-created_at')
    
    if query:
        participants = participants.filter(first_name__icontains=query) | participants.filter(last_name__icontains=query) | participants.filter(ndis_number__icontains=query)
        
    if status_filter:
        participants = participants.filter(status=status_filter)
        
    context = {
        'participants': participants,
        'query': query,
        'status_filter': status_filter,
    }
    return render(request, 'portal/participants/list.html', context)

@login_required(login_url='portal:login')
def participant_detail(request, pk):
    from django.shortcuts import get_object_or_404
    participant = get_object_or_404(Participant, pk=pk)
    return render(request, 'portal/participants/detail.html', {'participant': participant})

@login_required(login_url='portal:login')
def referral_list(request):
    query = request.GET.get('q', '')
    status_filter = request.GET.get('status', '')
    
    referrals = Referral.objects.all().order_by('-created_at')
    
    if query:
        referrals = referrals.filter(first_name__icontains=query) | referrals.filter(last_name__icontains=query)
        
    if status_filter:
        referrals = referrals.filter(status=status_filter)
        
    context = {
        'referrals': referrals,
        'query': query,
        'status_filter': status_filter,
    }
    return render(request, 'portal/referrals/list.html', context)

@login_required(login_url='portal:login')
def referral_detail(request, pk):
    from django.shortcuts import get_object_or_404
    referral = get_object_or_404(Referral, pk=pk)
    return render(request, 'portal/referrals/detail.html', {'referral': referral})

@login_required(login_url='portal:login')
def support_plans(request):
    return render(request, 'portal/placeholder.html', {'title': 'Support Plans'})

@login_required(login_url='portal:login')
def case_notes(request):
    return render(request, 'portal/placeholder.html', {'title': 'Case Notes'})

@login_required(login_url='portal:login')
def documents(request):
    return render(request, 'portal/placeholder.html', {'title': 'Documents'})

@login_required(login_url='portal:login')
def leave_requests(request):
    return render(request, 'portal/placeholder.html', {'title': 'Leave Requests'})

@login_required(login_url='portal:login')
def announcements(request):
    return render(request, 'portal/placeholder.html', {'title': 'Announcements'})

@login_required(login_url='portal:login')
def reports(request):
    return render(request, 'portal/placeholder.html', {'title': 'Reports'})

@login_required(login_url='portal:login')
def profile(request):
    return render(request, 'portal/placeholder.html', {'title': 'Profile'})


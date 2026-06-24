from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import FAQ

def contact_view(request):
    faqs = FAQ.objects.filter(is_active=True)
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully. We will get back to you shortly.')
            return redirect('contact:contact_us')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form below.')
    else:
        form = ContactForm()
        
    context = {
        'form': form,
        'faqs': faqs,
    }
    return render(request, 'contact/contact.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Count
from .models import Category, Blog, NewsletterSubscriber

def resource_list(request, category_slug=None):
    categories = Category.objects.annotate(article_count=Count('blogs'))
    
    search_query = request.GET.get('q', '')
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        articles = Blog.objects.filter(category=category, is_published=True)
    else:
        category = None
        articles = Blog.objects.filter(is_published=True)
        
    if search_query:
        articles = articles.filter(title__icontains=search_query)
        
    featured_article = Blog.objects.filter(is_featured=True, is_published=True).first()

    if request.method == 'POST' and 'newsletter_email' in request.POST:
        email = request.POST.get('newsletter_email')
        name = request.POST.get('newsletter_name', '')
        if email:
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email, name=name)
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                messages.info(request, 'You are already subscribed.')
            return redirect('resources:resource_list')

    context = {
        'categories': categories,
        'current_category': category,
        'articles': articles,
        'featured_article': featured_article,
        'search_query': search_query,
    }
    return render(request, 'resources/resource_list.html', context)


def article_detail(request, slug):
    article = get_object_or_404(Blog, slug=slug, is_published=True)
    categories = Category.objects.annotate(article_count=Count('blogs'))
    recent_articles = Blog.objects.filter(is_published=True).exclude(id=article.id).order_by('-created_at')[:4]
    related_articles = Blog.objects.filter(category=article.category, is_published=True).exclude(id=article.id)[:3]
    
    if request.method == 'POST' and 'newsletter_email' in request.POST:
        email = request.POST.get('newsletter_email')
        name = request.POST.get('newsletter_name', '')
        if email:
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email, name=name)
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                messages.info(request, 'You are already subscribed.')
            return redirect('resources:article_detail', slug=slug)

    context = {
        'article': article,
        'categories': categories,
        'recent_articles': recent_articles,
        'related_articles': related_articles,
    }
    return render(request, 'resources/article_detail.html', context)

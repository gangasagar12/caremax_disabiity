from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='blogs')
    featured_image = models.ImageField(upload_to='resources/images/')
    excerpt = models.TextField(help_text="Short description displayed on cards.")
    content = models.TextField(help_text="Main content of the article.")
    author = models.CharField(max_length=150, default='CareMax Disability')
    reading_time = models.IntegerField(help_text="Reading time in minutes.", default=5)
    
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    
    # SEO Fields
    meta_title = models.CharField(max_length=255, blank=True, null=True, help_text="SEO Title")
    meta_description = models.TextField(blank=True, null=True, help_text="Meta Description")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class NewsletterSubscriber(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"

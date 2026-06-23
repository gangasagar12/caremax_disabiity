from django.db import models

class ServiceCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Service Categories"

    def __str__(self):
        return self.title

class Service(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='services')
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    short_description = models.TextField()
    full_description = models.TextField()
    featured_image = models.ImageField(upload_to='services/', blank=True, null=True)
    icon = models.CharField(max_length=50, help_text='FontAwesome class e.g. "fas fa-home"')
    status = models.BooleanField(default=True, verbose_name="Active")

    def __str__(self):
        return self.title

class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="fas fa-check", help_text='FontAwesome class')

    def __str__(self):
        return self.title

class ServiceFAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

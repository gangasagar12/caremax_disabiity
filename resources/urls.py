from django.urls import path
from . import views

app_name = 'resources'

urlpatterns = [
    path('', views.resource_list, name='resource_list'),
    path('category/<slug:category_slug>/', views.resource_list, name='category_list'),
    path('<slug:slug>/', views.article_detail, name='article_detail'),
]

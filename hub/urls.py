from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_dating_hub, name='home'),
    path('about/', views.about, name='about'),
    path('pros-cons/', views.pros_cons, name='pros_cons'),  # Keep this name consistent
    path('known-websites/', views.known_websites, name='known_websites'),
    path('blog/', views.blog, name='blog'),
    path('blog/boundaries/', views.blog_boundaries, name='blog_boundaries'),
    path('blog/ai/', views.blog_ai, name='blog_ai'),
    path('blog/micromance/', views.blog_micromance, name='blog_micromance'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('subscribe-success/', views.subscribe_success, name='subscribe_success'),
]
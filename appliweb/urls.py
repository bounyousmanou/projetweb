from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('sujets/', views.liste_sujets, name='liste_sujets'),
    path('pricing/', views.pricing, name='pricing'),
    path('propos/', views.propos, name='propos'),
    path('contact/', views.envoyer_message, name='contact'),
    path('search/', views.search, name='search'),
    path('rechercher/', views.recherche_sujet, name='recherche_sujet'),
    path('sujets/<int:sujet_id>/', views.detail_sujet, name='detail_sujet'),
    path('ajouter/', views.ajouter_sujet, name='ajouter_sujet'),
] 


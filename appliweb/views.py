from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404, redirect
from appliweb.forms import SujetForm, ContactForm
from django.core.mail import send_mail
from .models import Sujet
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')

def pricing(request):
    return render(request, 'pricing.html')

def propos(request):
    return render(request, 'propos.html')

def custom_page_not_found_view(request, exception):
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "errors/400.html", {})

def envoyer_message(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Envoyer l'email
            send_mail(
                f'Message de {nom}',
                message,
                email,
                ['destinataire@example.com'], # Remplacez par votre adresse email de réception
                fail_silently=False,
            )
            return redirect('success_url') # Redirigez vers une page de succès
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

    
def search(request):
    # Récupérer les choix de filière, de niveau et de cours directement depuis le modèle
    type_sujet_choices = Sujet.TYPE_SUJET_CHOICES
    filiere_choices = Sujet.FILIERE_CHOICES
    niveau_choices = Sujet.NIVEAU_CHOICES
    return render(request, 'search.html', {
        'type_sujet_choices': type_sujet_choices,
        'filiere_choices': filiere_choices,
        'niveau_choices': niveau_choices
    })


def liste_sujets(request):
    # Récupérer les paramètres du formulaire
    type_sujet_choisi = request.GET.get('type_sujet')
    filiere_choisie = request.GET.get('filiere')
    niveau_choisi = request.GET.get('niveau')

    # Filtrer les sujets en fonction des paramètres du formulaire
    sujets = Sujet.objects.all()
    if filiere_choisie and niveau_choisi:
        sujets = sujets.filter(type_sujet=type_sujet_choisi)
        sujets = sujets.filter(filiere=filiere_choisie)
        sujets = sujets.filter(niveau=niveau_choisi)
    
    paginator = Paginator(sujets, 5) # 5 sujets par page
    # Récupérer le numéro de la page actuelle depuis la requête GET
    page_number = request.GET.get('page')
    # Récupérer les sujets pour la page actuelle
    page_obj = paginator.get_page(page_number)

    
    return render(request, 'liste_sujets.html', {'page_obj': page_obj, 'type_sujet_choisi': type_sujet_choisi,'filiere_choisie': filiere_choisie, 'niveau_choisi': niveau_choisi})

@login_required
def detail_sujet(request, sujet_id):
    sujet = get_object_or_404(Sujet, id=sujet_id)
    return render(request, 'detail_sujet.html', {'sujet': sujet})

def recherche_sujet(request):
    query = request.GET.get('q', '')  # Récupère la chaîne de recherche de la requête GET
    if query:
        # Filtre les sujets en fonction de la chaîne de recherche dans le titre, le code de cours ou l'année
        sujets = Sujet.objects.filter(
            Q(titre__icontains=query) | 
            Q(code_cours__icontains=query) |
            Q(annee__icontains=query) |
            Q(nom_cours__icontains=query) |
            Q(type_sujet__icontains=query) |
            Q(niveau__icontains=query) |
            Q(filiere__icontains=query) |
            Q(cours__icontains=query)
        )
    else:
        sujets = Sujet.objects.all()  # Si aucune recherche n'est effectuée, renvoie tous les sujets

    paginator = Paginator(sujets, 5) # 5 sujets par page
    # Récupérer le numéro de la page actuelle depuis la requête GET
    page_number = request.GET.get('page')
    # Récupérer les sujets pour la page actuelle
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'liste_sujets.html', {'page_obj': page_obj, 'query': query})

@login_required
@permission_required('is_superuser')
def ajouter_sujet(request):
    sujets = Sujet.objects.all()
    if request.method == 'POST':
        form = SujetForm(request.POST, request.FILES)
        if form.is_valid():
            sujet = form.save(commit=False)
            sujet.utilisateur = request.user
            sujet.save()
            messages.success(request, 'Le sujet a été ajouté avec succès.')
            return redirect('liste_sujets')
    else:
        form = SujetForm()
    return render(request, 'ajouter_sujet.html', {'form': form, 'sujets': sujets})

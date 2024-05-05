from django import forms
from .models import Sujet

class SujetForm(forms.ModelForm):
    class Meta:
        model = Sujet
        fields = ['titre', 'type_sujet', 'niveau', 'nom_cours', 'code_cours', 'annee', 'filiere', 'fichier']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'type_sujet': forms.Select(attrs={'class': 'form-control'}),
            'niveau': forms.Select(attrs={'class': 'form-control'}),
            'nom_cours': forms.TextInput(attrs={'class': 'form-control'}),
            'code_cours': forms.TextInput(attrs={'class': 'form-control'}),
            'annee': forms.NumberInput(attrs={'class': 'form-control'}),
            'sujet':  forms.HiddenInput(attrs={'class': 'form-control'}),
            'filiere': forms.Select(attrs={'class': 'form-control'}),
            'fichier': forms.FileInput(attrs={'class': 'form-control-file'}),
            'cours' : forms.Select(attrs={'class': 'form_control'}),
        }

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

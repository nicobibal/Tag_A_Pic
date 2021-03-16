from django.http import HttpResponse
from django.shortcuts import render
from .models import Image


def index(request):
    return render(request, 'Download/index.html')

def usernameForme(request):
    if request.method == 'POST':

        Image.downloadImageFromUsername(request.POST['username'])
        images =  Image.objects.all()
        print(images)

        return render(request, 'Download/index.html')

def afficher(request):
    images = Image.objects.all()
    return render(request, 'Download/images.html', {'images': images} )

def accueil(request):
    return render(request, 'GestionDossier/accueil_vue.html')

def connexion(request):
    return render(request, 'GestionDossier/connexion_vue.html')

def ajouterUser(request):
    return render(request, 'GestionDossier/ajouter_utilisateurs_vue.html')

def choixParam(request):
    return render(request, 'GestionDossier/choix_parametres_vue.html')

def erreur(request):
    return render(request, 'GestionDossier/erreur.html')

def gererUser(request):
    return render(request, 'GestionDossier/gerer_utilisateurs_vue.html')

def importer(request):
    return render(request, 'GestionDossier/importer_vue.html')

def modifUser(request):
    return render(request, 'GestionDossier/modifier_utilisateurs_vue.html')

def nouveauProjet(request):
    return render(request, 'GestionDossier/nouveau_projet_vue.html')

def nouvelUser(request):
    return render(request, 'GestionDossier/nouvel_utilisateur/vue.html')

def supprimerUser(request):
    return render(request, 'GestionDossier/supprimer_utilisateurs_vue.html')

def tag(request):
    return render(request, 'GestionDossier/tagger_vue.html')







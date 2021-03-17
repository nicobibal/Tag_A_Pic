from django.http import HttpResponse
from django.shortcuts import render
from .models import Image


def index(request):
    return render(request, 'Download/index.html')

def usernameForme(request):
    if request.method == 'POST':
        Image.downloadImageFromUsername(request.POST['username'], request.POST['nbPhotos'])
        return render(request, 'Download/index.html')

def usernameFormDate(request):
    if request.method == 'POST':
        Image.downloadPictureInSpecificPeriod(request.POST['dateStart'],request.POST['dateEnd'],request.POST['username'])
        return render(request, 'Download/index.html')

def usernameFormLiked(request):
    if request.method == 'POST':
        Image.downloadPictureMostLiked(request.POST['username'],request.POST['pourcentage'])
        return render(request, 'Download/index.html')

def afficher(request):
    images = Image.objects.all()
    return render(request, 'Download/images.html', {'images': images} )

def accueil(request):
    return render(request, 'Accueil/accueil_vue.html')

def connexion(request):
    return render(request, 'Connexion/connexion_vue.html')

def ajouterUser(request):
    return render(request, 'GestionUtilisateur/ajouter_utilisateurs_vue.html')

def choixParam(request):
    return render(request, 'Param/choix_parametres_vue.html')

def erreur(request):
    return render(request, 'Erreur/erreur.html')

def gererUser(request):
    return render(request, 'GestionUtilisateur/gerer_utilisateurs_vue.html')

def importer(request):
    return render(request, 'Importer/importer_vue.html')

def modifUser(request):
    return render(request, 'GestionUtilisateur/modifier_utilisateurs_vue.html')

def nouveauProjet(request):
    return render(request, 'GestionDossier/nouveau_projet_vue.html')

def nouvelUser(request):
    return render(request, 'GestionUtilisateur/nouvel_utilisateur_vue.html')

def supprimerUser(request):
    return render(request, 'GestionUtilisateur/supprimer_utilisateurs_vue.html')

def tag(request):
    return render(request, 'Tag/tagger_vue.html')







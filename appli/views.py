from django.http import HttpResponse
from django.shortcuts import render

from appli.forms import ImageForm
from appli.models.dossier import Dossier
from appli.models.image import Image
from appli.models.tag import Tag

def index(request):
    return render(request, 'Importer/import.html')

def usernameForme(request):
    if request.method == 'POST':
        Image.downloadImageFromUsername(request.POST['username'], request.POST['nbPhotos'])
        return render(request, 'Importer/import.html')

def usernameFormDate(request):
    if request.method == 'POST':
        Image.downloadPictureInSpecificPeriod(request.POST['dateStart'],request.POST['dateEnd'],request.POST['username'])
        return render(request, 'Importer/import.html')

def usernameFormLiked(request):
    if request.method == 'POST':
        Image.downloadPictureMostLiked(request.POST['username'],request.POST['pourcentage'])
        return render(request, 'Importer/import.html')

def afficher(request):
    images = Image.objects.all()
    return render(request, 'Download/images.html', {'images': images})

def accueil(request):
    return render(request, 'Accueil/accueil_vue.html')

def connexion(request):
    return render(request, 'Connexion/connexion_vue.html')

def dossier(request):
    dossiers = Dossier.objects.all()
    return render(request, 'Dossier/dossier.html',{'dossiers': dossiers})

def ajouterUser(request):
    return render(request, 'GestionUtilisateur/ajouter_utilisateurs_vue.html')

def choixParam(request):
    return render(request, 'Param/choix_parametres_vue.html')

def erreur(request):
    return render(request, 'Erreur/erreur.html')

def gererUser(request):
    return render(request, 'GestionUtilisateur/gerer_utilisateurs_vue.html')

def importer(request):
    return render(request, 'Importer/import.html')

def modifUser(request):
    return render(request, 'GestionUtilisateur/modifier_utilisateurs_vue.html')

def nouveauProjet(request):
    return render(request, 'GestionDossier/nouveau_projet_vue.html')

def nouvelUser(request):
    return render(request, 'GestionUtilisateur/nouvel_utilisateur_vue.html')

def supprimerUser(request):
    return render(request, 'GestionUtilisateur/supprimer_utilisateurs_vue.html')

def tag(request):
    if request.method == 'POST':
        tag = Tag(nom= request.POST['tag'])
        tag.save()
    tags = Tag.objects.all()
    return render(request, 'Tag/tagger_vue.html', {'tags' : tags})

def tagOneImage(request, image_id):
    image = Image.objects.get(pk=image_id)
    if request.method == 'POST':
        form = ImageForm(data=request.POST, instance=image)
        if form.is_valid():

            image = form.save(commit=False)
            image.save()
            form.save_m2m()
    else:
        form = ImageForm(instance=image)
    return render(request, 'Tag/tag_one_image.html',{'image' : image, 'image_form': form} )

def selection(request):
    tags = Tag.objects.order_by('nom')
    return render(request, 'Selection/selection.html', {'tags':tags})

def chercher(request):
    global images
    tags = request.POST.getlist('tag')

    if request.POST['selectionchoix'] == 'union':
        images=Image.objects.filter(tags__in=tags).distinct()

    if request.POST['selectionchoix'] == 'intersection':
        images = Image.objects
        for tag in tags:
            images = images.filter(tags__in=[tag])
    return render(request, 'Selection/resultatFiltre.html', {'images': images})

def faireDossier(request):

    dossier = Dossier(nom=request.POST['nomDossier'])
    dossier.save()
    for image in images:
        dossier.images.add(image)

    return render(request, 'Selection/resultatFiltre.html', {'images': images})

def ouvrirDossier(request, dossier_id):
    images = Image.objects.filter(dossier__pk=dossier_id)
    dossier = Dossier.objects.get(pk=dossier_id)
    return render(request, 'Dossier/ouvrirDossier.html', {'images': images, 'dossier':dossier})



def nuage(request):
    return render(request, 'Nuage/nuage.html')






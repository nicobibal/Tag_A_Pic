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



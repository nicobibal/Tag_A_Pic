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



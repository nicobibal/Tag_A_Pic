from django.http import HttpResponse
from django.shortcuts import render
from .models import Image


def index(request):
    return render(request,'index.html')

def usernameForme(request):
    if request.method == 'POST':

        Image.downloadImageFromUsername(request.POST['username'])
        return HttpResponse('Ca telecharge zebi')

    return render(request, 'username.html')

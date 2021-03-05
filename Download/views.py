from django.http import HttpResponse
from django.shortcuts import render
from .forms import usernameForm
from . import insta
from .models import Profil

def index(request):
    return render(request,'index.html')

def usernameForme(request):
    if request.method == 'POST':

        insta.downloadPicturesFromUsername(request.POST['username'])
        return HttpResponse('Ca telecharge zebi')
    else:
        form = usernameForm()
    return render(request, 'username.html', {'form' : form})

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('DownloadByUsername/', views.usernameForme),
    path('DownloadByDate/', views.usernameFormDate,),
    path('DownloadByLiked/', views.usernameFormLiked),
    path('afficher/', views.afficher),
]

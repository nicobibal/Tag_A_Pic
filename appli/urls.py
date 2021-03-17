from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('DownloadByUsername/', views.usernameForme),
    path('DownloadByDate/', views.usernameFormDate,),
    path('DownloadByLiked/', views.usernameFormLiked),
    path('afficher/', views.afficher),
    path('accueil/', views.accueil),
    path('connexion/', views.connexion),
    path('ajouterUser/', views.ajouterUser),
    path('choixParam/', views.choixParam),
    path('erreur/', views.erreur),
    path('gererUser/', views.gererUser),
    path('importer/', views.importer),
    path('modifUser/', views.modifUser),
    path('nouveauProjet/', views.nouveauProjet),
    path('nouvelUser/', views.nouvelUser),
    path('supprimerUser/', views.supprimerUser),
    path('tag/', views.tag),

]

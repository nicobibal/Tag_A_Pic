from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('go/', views.usernameForme, name='search'),
    path('afficher/', views.afficher),
]

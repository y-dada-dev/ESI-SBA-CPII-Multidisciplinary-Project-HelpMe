
from django.urls import path
from . import views
urlpatterns = [
    path("Sante.html", views.Sante, name="Sante"),
    path("education.html",views.education,name="education"),
    path("autres.html",views.autres,name="autres"),
    path("details.html/<int:id>",views.details,name="details"),
    path("", views.Accueil, name="Accueil"),
    path("Web_About_Us_Y.html",views.about, name = "about"),
    path("Association.html",views.association, name = "association"),


]

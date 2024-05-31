from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("libros", views.libros, name="libros"),
    path("registrarlibro", views.registrarLibros, name="registrarlibros"),
    path("autor", views.autores, name="autor"),
    path("registrarautor", views.registrarAutor, name="registrarautor"),
]
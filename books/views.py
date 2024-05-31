from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def index(request):
    return render(request, "index.html")

def libros(request):
    libros = Libro.objects.all()
    context = {"libros":libros}
    return render(request, "libros.html",context)

def autores(request):
    autores = Autor.objects.all()
    context = {"autores":autores}
    return render(request, "autores.html",context)
def registrarLibros(request):
    if request.method == "GET":
        editoriales = Editorial.objects.all()
        autores = Autor.objects.all()
        generos = Genero.objects.all()
        context = {"autores":autores,"editoriales":editoriales,"generos":generos}
        return render(request,"registrarlibro.html",context)
    if request.method == "POST":
        print(request.POST)
        #Crea el Libro
        nombre_libro = request.POST["nombrelibro"]
        codigo_libro = request.POST["codigolibro"]
        existencias = request.POST["existencias"]
        precio = request.POST["precio"]
        autor = request.POST["autor"]
        editorial = request.POST["editorial"]
        genero = request.POST["genero"]
        descripcion = request.POST["descripcion"]
        authorinstance = Autor.objects.get(codigo_autor=autor)
        editorialinstance = Editorial.objects.get(codigo_editorial=editorial)
        generointance = Genero.objects.get(id_genero=genero)
        Libro.objects.create(nombre_libro=nombre_libro,codigo_libro=codigo_libro,existencias=existencias,precio=precio,codigo_autor=authorinstance,
                             codigo_editorial=editorialinstance,id_genero=generointance,descripcion=descripcion)

        return redirect("libros")

def registrarAutor(request):
    if request.method == "GET":
        return render(request,"registrarautor.html")
    if request.method == "POST":
        print(request.POST)
        #Crea el autor
        nombre_autor = request.POST["nombreautor"]
        codigo_autor = request.POST["codigoautor"]
        nacio = request.POST["nacionalidad"]
        Autor.objects.create()

        return redirect("autor")

def editorial(request):
    editorial = Editorial.objects.all()
    return render(request, "editorial.html")
# Create your views here
from django.contrib import admin
from .models import Autor, Genero, Editorial, Libro

class AutorAdmin(admin.ModelAdmin):
    list_display = ('codigo_autor', 'nombre_autor', 'nacionalidad')
    search_fields = ('nombre_autor', 'nacionalidad')

class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id_genero', 'nombre_genero', 'descripcion')
    search_fields = ('nombre_genero',)

class EditorialAdmin(admin.ModelAdmin):
    list_display = ('codigo_editorial', 'nombre_editorial', 'contacto', 'telefono')
    search_fields = ('nombre_editorial', 'contacto')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('codigo_libro', 'nombre_libro', 'existencias', 'precio', 'codigo_autor', 'codigo_editorial', 'id_genero')
    search_fields = ('nombre_libro',)
    list_filter = ('codigo_autor', 'codigo_editorial', 'id_genero')

admin.site.register(Autor, AutorAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Libro, LibroAdmin)
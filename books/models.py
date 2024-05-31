from django.db import models

class Autor(models.Model):
    codigo_autor = models.CharField(max_length=6, primary_key=True)
    nombre_autor = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_autor

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_genero

class Editorial(models.Model):
    codigo_editorial = models.CharField(max_length=6, primary_key=True)
    nombre_editorial = models.CharField(max_length=30)
    contacto = models.CharField(max_length=30)
    telefono = models.CharField(max_length=9)

    def __str__(self):
        return self.nombre_editorial

class Libro(models.Model):
    codigo_libro = models.CharField(max_length=9, primary_key=True)
    nombre_libro = models.CharField(max_length=50)
    existencias = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    codigo_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre_libro

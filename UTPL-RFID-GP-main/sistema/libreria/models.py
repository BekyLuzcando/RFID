from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    abstract = models.TextField(verbose_name= "Descripción",null=True)
    stock_actual = models.IntegerField(blank=True, null=True)
    stock_total= models.IntegerField(blank=True, null=True)
    fecha_publicacion= models.DateField()
    numero_paginas= models.IntegerField(blank=True, null=True)
    editorial=models.TextField(max_length=900)
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen",null = True)
    codigo = models.TextField(verbose_name = "Codigo",null = True)

    def __str__(self):
        fila = "Titulo: " + self.titulo +  " - " + "Codigo: " + self.codigo
        return fila

    def delete(self, using=None, keep_parents = False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete
        
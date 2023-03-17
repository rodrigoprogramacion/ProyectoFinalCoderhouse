from django.db import models
from django.contrib.auth.models import User #importacion de la clase User

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    #clase meta para darle nombre a las tablas
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    #metodo string para devolver titulos
    def __str__(self):
        return self.nombre
    
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=500)
    imagen=models.ImageField(upload_to='AppBlog', null=True, blank=True)#agregar imagenes opcionalmente
    autor=models.ForeignKey(User, on_delete=models.CASCADE)#relacion tabla user-posts eliminacion en cascada relacion uno a varios
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
    categorias=models.ManyToManyField(Categoria)#establece relacion varios a varios en la base de datos

    #clase meta para darle nombre a las tablas
    class Meta:
        verbose_name='post'
        verbose_name_plural='posteos'
    #metodo string para devolver titulos
    def __str__(self):
        return self.titulo
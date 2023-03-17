from django.contrib import admin
from .models import Categoria, Post
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):#herencia de la clase modeladmin
    readonly_fields=('created','updated')#clase que crea las fechas de automaticamente

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Categoria, CategoriaAdmin) #con el metodo register() cargamos los modelos en el panel de administracion de django
admin.site.register(Post, PostAdmin)

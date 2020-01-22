from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=200, verbose_name='Nombre')
    created= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated= models.DateTimeField(auto_now=True, verbose_name='Fecha de ultima Modificación')

    class Meta:
        verbose_name= "Categoria"
        verbose_name_plural= "Categorias"
        ordering = ["-created"]

    def __str__(self,):
        return self.name

class post(models.Model):
    title= models.CharField(max_length=200, verbose_name='Titulo del post')
    content= models.TextField(verbose_name='Contenido')
    published= models.DateTimeField(verbose_name='Fecha de publicación', default=now)
    image= models.ImageField(verbose_name='Imagen', upload_to='blog', blank=True, null=True)
    author= models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories= models.ManyToManyField(Category, verbose_name="Categorias", related_name="get_post")
    created= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated= models.DateTimeField(auto_now=True, verbose_name='Fecha de ultima Modificación')

    class Meta:
        verbose_name= "Publicacion"
        verbose_name_plural= "Publicaciones"
        ordering = ["-created"]

    def __str__(self,):
        return self.title
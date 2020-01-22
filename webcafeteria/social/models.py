from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre Clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Nombre", max_length=200)
    link = models.URLField(verbose_name="Enlace", blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated= models.DateTimeField(auto_now=True, verbose_name='Fecha de ultima Modificación')

    class Meta:
        verbose_name= "Enlace"
        verbose_name_plural= "Enlaces"
        ordering = ["key"]

    def __str__(self,):
        return self.key

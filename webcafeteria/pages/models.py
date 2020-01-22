from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pages(models.Model):
    name = models.CharField(verbose_name="Nombre", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated= models.DateTimeField(auto_now=True, verbose_name='Fecha de ultima Modificación')

    class Meta:
        verbose_name= "Pagina"
        verbose_name_plural= "Paginas"
        ordering = ["order", "name"]

    def __str__(self,):
        return self.name

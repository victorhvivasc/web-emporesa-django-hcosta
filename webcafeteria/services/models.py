from django.db import models

# Create your models here.
class service(models.Model):
    title= models.CharField(max_length=200, verbose_name='Nombre del servicio')
    subtitle= models.CharField(max_length=200, verbose_name='Descripción breve')
    content= models.TextField(verbose_name='Descripción detallada')
    image= models.ImageField(verbose_name='Imagen', upload_to='services')
    created= models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated= models.DateTimeField(auto_now=True, verbose_name='Fecha de ultima Modificación')

    class Meta:
        verbose_name= 'Servicio'
        verbose_name_plural= 'Servicios'
    
    def __str__(self):
        return self.title

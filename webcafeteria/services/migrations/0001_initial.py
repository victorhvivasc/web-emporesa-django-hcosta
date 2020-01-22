# Generated by Django 3.0.2 on 2020-01-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Nombre del servicio')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Descripción breve')),
                ('content', models.TextField(verbose_name='Descripción detallada')),
                ('image', models.ImageField(upload_to='services', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de ultima Modificación')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
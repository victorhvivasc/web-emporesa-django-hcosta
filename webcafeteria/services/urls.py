from django.contrib import admin
from django.urls import path, include
from services import views

from django.conf import settings


urlpatterns = [
    path('', views.service, name="servicios"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
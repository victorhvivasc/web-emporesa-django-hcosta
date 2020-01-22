from django.urls import path
from core import views

from django.conf import settings

urlpatterns = [
    path('', views.home, name="inicio"), 
    path('about/', views.about, name="acerca"),
    path('store/', views.store, name="visitanos"),
    ]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
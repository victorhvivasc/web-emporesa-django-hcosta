from django.urls import path
from blog import views

from django.conf import settings

urlpatterns = [
    path('', views.Blog, name="blog"),  
    path('category/<int:category_id>', views.category, name="cat"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
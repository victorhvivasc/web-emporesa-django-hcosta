from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:Pages_id>/', views.Sample, name="muestra"),
]


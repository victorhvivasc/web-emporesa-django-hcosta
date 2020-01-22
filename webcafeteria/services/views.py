from django.shortcuts import render
from .models import service as ser

# Create your views here.

def service(request):
    servicios = ser.objects.all()
    return render(request, "services/services.html", {'arepa': servicios})


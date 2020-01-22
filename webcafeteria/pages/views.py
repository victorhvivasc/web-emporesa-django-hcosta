from django.shortcuts import render, get_object_or_404
from .models import Pages

# Create your views here.

def Sample(request, Pages_id):
    page= get_object_or_404(Pages, id=Pages_id)
    return render(request, "pages/sample.html", {"pagina": page})



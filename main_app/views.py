from django.shortcuts import render
from .models import Convo

# Create your views here.
def index(request):
    convos = Convo.objects.all()
    return render(request, 'index.html', {'convos' : convos})

from django.shortcuts import render

from .models import About
# Create your views here.
def home(request):
    about = About.objects
    return render(request, 'about/home.html', { 'about': about})
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def stands_index(request):
    return render(request, 'stands/index.html')


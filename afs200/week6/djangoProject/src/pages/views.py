from django.http import HttpResponse, request
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})

def about(request, *args, **kwargs):
    return render(request, "about.html", {})

def contact(request, *args, **kwargs):
    return render(request, "contact.html", {})
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def index(request):
    return render(request, "homepage.html")

def start_scanning(request):
    return render(request, "start-scanning.html")

def create_account(request):
    return render(request, "healthcare-create-account.html")
    
def login(request):
    return render(request, "healthcare-login.html")
    
def provider(request):
    return render(request, "healthcare-provider.html")
    
def submitted(request):
    return render(request, "healthcare-submitted.html")
    
def provider_scan(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('submitted/')
    else:
        form = ImageForm()
    return render(request, 'provider-scan.html', {'form' : form})
    
def results(request):
    return render(request, "results.html")
    
def about(request):
    return render(request, "about.html")
    


    
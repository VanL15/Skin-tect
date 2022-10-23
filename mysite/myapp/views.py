from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .predict import predict

# Create your views here.
def index(request):
    return render(request, "homepage.html")

def start_scanning(request):
    if request.method == 'POST':
        form = ImageForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            print(predict(r"C:\Users\james\Desktop\skin-cancer-validation\mysite\media\images" + "\\" + str(img_obj)))
            return render(request, ('results.html'))
    else:
        form = ImageForm()
    return render(request, "start-scanning.html", {'form' : form})

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
            img_obj = form.instance
            return render(request, ('healthcare-submitted.html'))
    else:
        form = ImageForm()
    return render(request, 'provider-scan.html', {'form' : form})
    
def results(request):
    return render(request, "results.html")
    
def about(request):
    return render(request, "about.html")
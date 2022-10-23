from django.shortcuts import render

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
    return render(request, "provider-scan.html")
    
def results(request):
    return render(request, "results.html")
    
def about(request):
    return render(request, "about.html")
    


    
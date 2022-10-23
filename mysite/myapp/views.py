from django.shortcuts import render
from .forms import ImageForm

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
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'provider-scan.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'provider-scan.html', {'form': form})
    
def results(request):
    return render(request, "results.html")
    
def about(request):
    return render(request, "about.html")
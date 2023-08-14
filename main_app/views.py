from django.shortcuts import render

# Define view functions here

def home(request):
    #pass request object first
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
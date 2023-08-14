from django.shortcuts import render

# Define view functions here

def home(request):
    #pass request object first
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finch_index(request):
    #search the db for ALL of the cats
    finches = Finch.objects.all()

    #respond to the client, by injecting the finch list we found from the db into our finches/index.html template

